/********************************************************************************
** Form generated from reading UI file 'rfidAntennaProperties.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_RFIDANTENNAPROPERTIES_H
#define UI_RFIDANTENNAPROPERTIES_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_RfidAntennaProperties
{
public:
    QGridLayout *gridLayout_2;
    QGridLayout *gridLayout;
    QLineEdit *rfidY;
    QLineEdit *rfidAngleSpan;
    QLineEdit *rfidSignalCutoff;
    QLineEdit *rfidMaxDistance;
    QLabel *label_6;
    QLineEdit *rfidX;
    QLabel *label_5;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_2;
    QLabel *label;
    QLineEdit *rfidOrientation;
    QLabel *label_7;
    QLineEdit *rfidFrequency;
    QHBoxLayout *horizontalLayout;
    QPushButton *pushButton;
    QPushButton *refreshRfid;

    void setupUi(QWidget *RfidAntennaProperties)
    {
        if (RfidAntennaProperties->objectName().isEmpty())
            RfidAntennaProperties->setObjectName(QString::fromUtf8("RfidAntennaProperties"));
        RfidAntennaProperties->resize(289, 280);
        gridLayout_2 = new QGridLayout(RfidAntennaProperties);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        rfidY = new QLineEdit(RfidAntennaProperties);
        rfidY->setObjectName(QString::fromUtf8("rfidY"));
        rfidY->setReadOnly(false);

        gridLayout->addWidget(rfidY, 5, 1, 1, 1);

        rfidAngleSpan = new QLineEdit(RfidAntennaProperties);
        rfidAngleSpan->setObjectName(QString::fromUtf8("rfidAngleSpan"));

        gridLayout->addWidget(rfidAngleSpan, 0, 1, 1, 1);

        rfidSignalCutoff = new QLineEdit(RfidAntennaProperties);
        rfidSignalCutoff->setObjectName(QString::fromUtf8("rfidSignalCutoff"));

        gridLayout->addWidget(rfidSignalCutoff, 3, 1, 1, 1);

        rfidMaxDistance = new QLineEdit(RfidAntennaProperties);
        rfidMaxDistance->setObjectName(QString::fromUtf8("rfidMaxDistance"));

        gridLayout->addWidget(rfidMaxDistance, 2, 1, 1, 1);

        label_6 = new QLabel(RfidAntennaProperties);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout->addWidget(label_6, 3, 0, 1, 1);

        rfidX = new QLineEdit(RfidAntennaProperties);
        rfidX->setObjectName(QString::fromUtf8("rfidX"));
        rfidX->setReadOnly(false);

        gridLayout->addWidget(rfidX, 4, 1, 1, 1);

        label_5 = new QLabel(RfidAntennaProperties);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout->addWidget(label_5, 5, 0, 1, 1);

        label_3 = new QLabel(RfidAntennaProperties);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        label_4 = new QLabel(RfidAntennaProperties);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 4, 0, 1, 1);

        label_2 = new QLabel(RfidAntennaProperties);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 0, 0, 1, 1);

        label = new QLabel(RfidAntennaProperties);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 1, 0, 1, 1);

        rfidOrientation = new QLineEdit(RfidAntennaProperties);
        rfidOrientation->setObjectName(QString::fromUtf8("rfidOrientation"));

        gridLayout->addWidget(rfidOrientation, 1, 1, 1, 1);

        label_7 = new QLabel(RfidAntennaProperties);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout->addWidget(label_7, 6, 0, 1, 1);

        rfidFrequency = new QLineEdit(RfidAntennaProperties);
        rfidFrequency->setObjectName(QString::fromUtf8("rfidFrequency"));

        gridLayout->addWidget(rfidFrequency, 6, 1, 1, 1);


        gridLayout_2->addLayout(gridLayout, 0, 0, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        pushButton = new QPushButton(RfidAntennaProperties);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setMaximumSize(QSize(100, 16777215));

        horizontalLayout->addWidget(pushButton);

        refreshRfid = new QPushButton(RfidAntennaProperties);
        refreshRfid->setObjectName(QString::fromUtf8("refreshRfid"));
        refreshRfid->setMinimumSize(QSize(100, 0));
        refreshRfid->setMaximumSize(QSize(100, 16777215));

        horizontalLayout->addWidget(refreshRfid);


        gridLayout_2->addLayout(horizontalLayout, 1, 0, 1, 1);

        QWidget::setTabOrder(rfidAngleSpan, rfidOrientation);
        QWidget::setTabOrder(rfidOrientation, rfidMaxDistance);
        QWidget::setTabOrder(rfidMaxDistance, rfidSignalCutoff);
        QWidget::setTabOrder(rfidSignalCutoff, rfidX);
        QWidget::setTabOrder(rfidX, rfidY);
        QWidget::setTabOrder(rfidY, rfidFrequency);
        QWidget::setTabOrder(rfidFrequency, pushButton);
        QWidget::setTabOrder(pushButton, refreshRfid);

        retranslateUi(RfidAntennaProperties);

        QMetaObject::connectSlotsByName(RfidAntennaProperties);
    } // setupUi

    void retranslateUi(QWidget *RfidAntennaProperties)
    {
        RfidAntennaProperties->setWindowTitle(QApplication::translate("RfidAntennaProperties", "RFID Antenna", nullptr));
        rfidY->setText(QApplication::translate("RfidAntennaProperties", "0.0", nullptr));
        rfidAngleSpan->setText(QApplication::translate("RfidAntennaProperties", "360", nullptr));
        rfidSignalCutoff->setText(QApplication::translate("RfidAntennaProperties", "0.3", nullptr));
        rfidMaxDistance->setText(QApplication::translate("RfidAntennaProperties", "3.0", nullptr));
        label_6->setText(QApplication::translate("RfidAntennaProperties", "Signal prob. cutoff", nullptr));
        rfidX->setText(QApplication::translate("RfidAntennaProperties", "0.0", nullptr));
        label_5->setText(QApplication::translate("RfidAntennaProperties", "Translation - y (m)", nullptr));
        label_3->setText(QApplication::translate("RfidAntennaProperties", "Max distance (m)", nullptr));
        label_4->setText(QApplication::translate("RfidAntennaProperties", "Translation - x (m)", nullptr));
        label_2->setText(QApplication::translate("RfidAntennaProperties", "Angle span (degrees)", nullptr));
        label->setText(QApplication::translate("RfidAntennaProperties", "Orientation", nullptr));
        label_7->setText(QApplication::translate("RfidAntennaProperties", "Frequency", nullptr));
        pushButton->setText(QApplication::translate("RfidAntennaProperties", "Update", nullptr));
        refreshRfid->setText(QApplication::translate("RfidAntennaProperties", "Refresh", nullptr));
    } // retranslateUi

};

namespace Ui {
    class RfidAntennaProperties: public Ui_RfidAntennaProperties {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_RFIDANTENNAPROPERTIES_H
