# Adapted from https://github.com/rddy/ReQueST/blob/master/rqst/encoder_models.py

from __future__ import division

import os

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from .models import TFModel
from . import utils


class EncoderModel(TFModel):

  def encode_batch_frames(self, obses):
    """
    Args:
     obses: a np.array with dimensions (batch_size, W, H, C)
    Returns:
     a np.array with dimensions (batch_size, n_z_dim)
    """
    return self.encode(self.squash_obs(obses))

  def decode_batch_latents(self, latents):
    """
    Args:
     latents: a np.array with dimensions (batch_size, n_z_dim)
    Returns:
     a np.array with dimensions (batch_size, W, H, C)
    """
    return self.decode(latents)

  def squash_obs(self, obs):
    """
    Args:
     obs: a np.array with dimensions (batch_size, W, H, C) or (W, H, C)
    Returns:
     a np.array with dimensions (batch_size, W, H, C) or (W, H, C)
     copy of obs, with pixel values squashed to [0, 1]
    """
    obs_max = obs.max()
    obs_norm = 255. if obs_max > 1. else 1.
    return obs / obs_norm

  def encode_frame(self, obs):
    """
    Args:
     obs: a np.array with dimensions (W, H, C)
    Returns:
     a np.array with dimensions (n_z_dim)
    """
    return self.encode(self.squash_obs(obs[np.newaxis, :, :, :]))[0, :]

  def decode_latent(self, latent):
    """
    Args:
     latent: a np.array with dimensions (n_z_dim)
    Returns:
     a np.array with dimensions (W, H, C)
    """
    return (self.decode(latent[np.newaxis, :])[0, :, :, :] * 255).astype('uint8')


class VAEModel(EncoderModel):
  """Adapted from https://github.com/hardmaru/WorldModelsExperiments/blob/master/carracing/"""

  def __init__(
    self,
    *args,
    kl_tolerance=0.5,
    rnn_size=256,
    n_z_dim=32,
    **kwargs
    ):

    super().__init__(*args, **kwargs)

    self.rnn_size = rnn_size
    self.n_z_dim = n_z_dim

    self.data_keys = ['obses']

    # takes frames generated by utils.process_frame
    input_shape = [None, 64, 64, 3]
    self.input_x_ph = tf.placeholder(tf.float32, shape=input_shape)

    with tf.variable_scope(self.scope, reuse=tf.AUTO_REUSE):
      vae_out_vars = self.build_vae_net(self.input_x_ph)
    self.__dict__.update(vae_out_vars)

    if 'loss' not in vae_out_vars:
      # reconstruction
      r_loss = tf.reduce_sum(
          tf.square(self.input_x_ph - self.output_y),
          reduction_indices=[1, 2, 3])
      r_loss = tf.reduce_mean(r_loss)

      # regularization
      kl_loss = -0.5 * tf.reduce_sum(
          (1 + self.logvar - tf.square(self.mu) - tf.exp(self.logvar)),
          reduction_indices=1)
      kl_loss = tf.maximum(kl_loss, kl_tolerance * self.n_z_dim)
      kl_loss = tf.reduce_mean(kl_loss)

      self.loss = r_loss + kl_loss

  def build_encoder(self, input_x):
    h = tf.layers.conv2d(
        input_x, 32, 4, strides=2, activation=tf.nn.relu, name='enc_conv1')
    h = tf.layers.conv2d(
        h, 64, 4, strides=2, activation=tf.nn.relu, name='enc_conv2')
    h = tf.layers.conv2d(
        h, 128, 4, strides=2, activation=tf.nn.relu, name='enc_conv3')
    h = tf.layers.conv2d(
        h, 256, 4, strides=2, activation=tf.nn.relu, name='enc_conv4')
    h = tf.reshape(h, [tf.shape(h)[0], 2 * 2 * 256])
    return h

  def build_decoder(self, code_z):
    h = tf.layers.dense(code_z, 2 * 2 * 256, name='dec_fc')
    h = tf.reshape(h, [tf.shape(code_z)[0], 1, 1, 2 * 2 * 256])
    h = tf.layers.conv2d_transpose(
        h, 128, 5, strides=2, activation=tf.nn.relu, name='dec_deconv1')
    h = tf.layers.conv2d_transpose(
        h, 64, 5, strides=2, activation=tf.nn.relu, name='dec_deconv2')
    h = tf.layers.conv2d_transpose(
        h, 32, 6, strides=2, activation=tf.nn.relu, name='dec_deconv3')
    output_y = tf.layers.conv2d_transpose(
        h, 3, 6, strides=2, activation=tf.nn.sigmoid, name='dec_deconv4')
    return output_y

  def build_vae_net(self, input_x):
    h = self.build_encoder(input_x)

    mu = tf.layers.dense(h, self.n_z_dim, name='enc_fc_mu')
    logvar = tf.layers.dense(h, self.n_z_dim, name='enc_fc_log_var')
    sigma = tf.exp(logvar / 2.0)
    epsilon = tf.random_normal(tf.shape(mu))
    code_z = mu + sigma * epsilon

    output_y = self.build_decoder(code_z)
    output_y = tf.clip_by_value(output_y, 1e-8, 1 - 1e-8)

    return {
        'code_z': code_z,
        'output_y': output_y,
        'mu': mu,
        'logvar': logvar,
        'sigma': sigma,
        'epsilon': epsilon
    }

  def format_batch(self, batch):
    """
    Args:
     batch: a dict containing the output of a call to rqst.utils.vectorize_rollouts
      batch['obses'] maps to a np.array with dimensions (batch_size, W, H, C)
    Returns:
      a dict containing the input for a call to rqst.models.TFModel.compute_batch_loss
    """
    feed_dict = {self.input_x_ph: self.squash_obs(batch['obses'].astype(float))}
    return feed_dict

  def encode(self, input_x):
    """
    Args:
     input_x: a np.array with dimensions (batch_size, W, H, C)
    Returns:
     a np.array with dimensions (batch_size, n_z_dim)
    """
    feed_dict = {self.input_x_ph: input_x}
    return self.sess.run(self.mu, feed_dict=feed_dict)

  def encode_mu_logvar(self, input_x):
    """Useful for rqst.dynamics_models.MDNRNNDynamicsModel.preproc_rollouts
    Args:
     input_x: np (batch_size, W, H, C)
    Returns:
     a tuple containing (a np.array with dimensions (batch_size, n_z_dim),
      a np.array with dimensions (batch_size, n_z_dim))
    """
    feed_dict = {self.input_x_ph: self.squash_obs(input_x)}
    mu, logvar = self.sess.run([self.mu, self.logvar], feed_dict=feed_dict)
    return mu, logvar

  def decode(self, code_z):
    """
    Args:
     code_z: a np.array with dimensions (batch_size, n_z_dim)
    Returns:
     a np.array with dimensions (batch_size, W, H, C)
    """
    feed_dict = {self.code_z: code_z}
    return self.sess.run(self.output_y, feed_dict=feed_dict)

  def log_prob_latent(self, latent):
    """
    Args:
     latent: a tf.Tensor with dimensions (n_z_dim)
    Returns:
     a tf.Tensor with dimensions (1)
    """
    return -tf.reduce_mean(latent**2)


def load_wm_pretrained_vae(sess):
  scope = 'conv_vae'
  jsonfile = os.path.join(utils.wm_dir, 'vae', 'vae.json')
  encoder = VAEModel(
      sess,
      learning_rate=0.0001,
      kl_tolerance=0.5,
      rnn_size=256,
      n_z_dim=32,
      scope=scope,
      scope_file=os.path.join(utils.car_data_dir, 'enc_scope.pkl'),
      tf_file=os.path.join(utils.car_data_dir, 'enc.tf'))
  utils.load_wm_pretrained_model(jsonfile, scope, sess)
  return encoder
