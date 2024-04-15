# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "proj2_pkg: 2 messages, 0 services")

set(MSG_I_FLAGS "-Iproj2_pkg:/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(proj2_pkg_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg" NAME_WE)
add_custom_target(_proj2_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "proj2_pkg" "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg" ""
)

get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg" NAME_WE)
add_custom_target(_proj2_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "proj2_pkg" "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proj2_pkg
)
_generate_msg_cpp(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proj2_pkg
)

### Generating Services

### Generating Module File
_generate_module_cpp(proj2_pkg
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proj2_pkg
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(proj2_pkg_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(proj2_pkg_generate_messages proj2_pkg_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_cpp _proj2_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_cpp _proj2_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proj2_pkg_gencpp)
add_dependencies(proj2_pkg_gencpp proj2_pkg_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proj2_pkg_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proj2_pkg
)
_generate_msg_eus(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proj2_pkg
)

### Generating Services

### Generating Module File
_generate_module_eus(proj2_pkg
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proj2_pkg
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(proj2_pkg_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(proj2_pkg_generate_messages proj2_pkg_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_eus _proj2_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_eus _proj2_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proj2_pkg_geneus)
add_dependencies(proj2_pkg_geneus proj2_pkg_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proj2_pkg_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proj2_pkg
)
_generate_msg_lisp(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proj2_pkg
)

### Generating Services

### Generating Module File
_generate_module_lisp(proj2_pkg
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proj2_pkg
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(proj2_pkg_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(proj2_pkg_generate_messages proj2_pkg_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_lisp _proj2_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_lisp _proj2_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proj2_pkg_genlisp)
add_dependencies(proj2_pkg_genlisp proj2_pkg_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proj2_pkg_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proj2_pkg
)
_generate_msg_nodejs(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proj2_pkg
)

### Generating Services

### Generating Module File
_generate_module_nodejs(proj2_pkg
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proj2_pkg
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(proj2_pkg_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(proj2_pkg_generate_messages proj2_pkg_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_nodejs _proj2_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_nodejs _proj2_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proj2_pkg_gennodejs)
add_dependencies(proj2_pkg_gennodejs proj2_pkg_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proj2_pkg_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proj2_pkg
)
_generate_msg_py(proj2_pkg
  "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proj2_pkg
)

### Generating Services

### Generating Module File
_generate_module_py(proj2_pkg
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proj2_pkg
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(proj2_pkg_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(proj2_pkg_generate_messages proj2_pkg_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleStateMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_py _proj2_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cc/ee106b/sp24/class/ee106b-abh/EECS-C206B/project2/src/proj2_pkg/msg/BicycleCommandMsg.msg" NAME_WE)
add_dependencies(proj2_pkg_generate_messages_py _proj2_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(proj2_pkg_genpy)
add_dependencies(proj2_pkg_genpy proj2_pkg_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS proj2_pkg_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proj2_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/proj2_pkg
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(proj2_pkg_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(proj2_pkg_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET std_srvs_generate_messages_cpp)
  add_dependencies(proj2_pkg_generate_messages_cpp std_srvs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proj2_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/proj2_pkg
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(proj2_pkg_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(proj2_pkg_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET std_srvs_generate_messages_eus)
  add_dependencies(proj2_pkg_generate_messages_eus std_srvs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proj2_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/proj2_pkg
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(proj2_pkg_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(proj2_pkg_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET std_srvs_generate_messages_lisp)
  add_dependencies(proj2_pkg_generate_messages_lisp std_srvs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proj2_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/proj2_pkg
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(proj2_pkg_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(proj2_pkg_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET std_srvs_generate_messages_nodejs)
  add_dependencies(proj2_pkg_generate_messages_nodejs std_srvs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proj2_pkg)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proj2_pkg\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proj2_pkg
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  string(REGEX REPLACE "([][+.*()^])" "\\\\\\1" ESCAPED_PATH "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proj2_pkg")
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/proj2_pkg
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${ESCAPED_PATH}/.+/__init__.pyc?$"
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(proj2_pkg_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(proj2_pkg_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET std_srvs_generate_messages_py)
  add_dependencies(proj2_pkg_generate_messages_py std_srvs_generate_messages_py)
endif()
