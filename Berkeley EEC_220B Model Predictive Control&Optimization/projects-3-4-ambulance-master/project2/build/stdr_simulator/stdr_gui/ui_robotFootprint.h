/********************************************************************************
** Form generated from reading UI file 'robotFootprint.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ROBOTFOOTPRINT_H
#define UI_ROBOTFOOTPRINT_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_RobotFootprint
{
public:
    QGridLayout *gridLayout_2;
    QGridLayout *gridLayout;
    QLineEdit *robotFootprintX;
    QLabel *label_3;
    QLabel *label_2;
    QLineEdit *robotFootprintY;
    QHBoxLayout *horizontalLayout;
    QPushButton *updateButton;
    QPushButton *refresh_robot;

    void setupUi(QWidget *RobotFootprint)
    {
        if (RobotFootprint->objectName().isEmpty())
            RobotFootprint->setObjectName(QString::fromUtf8("RobotFootprint"));
        RobotFootprint->resize(348, 126);
        gridLayout_2 = new QGridLayout(RobotFootprint);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        robotFootprintX = new QLineEdit(RobotFootprint);
        robotFootprintX->setObjectName(QString::fromUtf8("robotFootprintX"));

        gridLayout->addWidget(robotFootprintX, 0, 1, 1, 1);

        label_3 = new QLabel(RobotFootprint);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 1, 0, 1, 1);

        label_2 = new QLabel(RobotFootprint);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 0, 0, 1, 1);

        robotFootprintY = new QLineEdit(RobotFootprint);
        robotFootprintY->setObjectName(QString::fromUtf8("robotFootprintY"));

        gridLayout->addWidget(robotFootprintY, 1, 1, 1, 1);


        gridLayout_2->addLayout(gridLayout, 0, 0, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        updateButton = new QPushButton(RobotFootprint);
        updateButton->setObjectName(QString::fromUtf8("updateButton"));
        updateButton->setMaximumSize(QSize(100, 16777215));

        horizontalLayout->addWidget(updateButton);

        refresh_robot = new QPushButton(RobotFootprint);
        refresh_robot->setObjectName(QString::fromUtf8("refresh_robot"));
        refresh_robot->setMaximumSize(QSize(100, 16777215));

        horizontalLayout->addWidget(refresh_robot);


        gridLayout_2->addLayout(horizontalLayout, 2, 0, 1, 1);

        QWidget::setTabOrder(robotFootprintX, robotFootprintY);

        retranslateUi(RobotFootprint);

        QMetaObject::connectSlotsByName(RobotFootprint);
    } // setupUi

    void retranslateUi(QWidget *RobotFootprint)
    {
        RobotFootprint->setWindowTitle(QApplication::translate("RobotFootprint", "Robot", nullptr));
        robotFootprintX->setText(QApplication::translate("RobotFootprint", "0.0", nullptr));
        label_3->setText(QApplication::translate("RobotFootprint", "y", nullptr));
        label_2->setText(QApplication::translate("RobotFootprint", "x", nullptr));
        robotFootprintY->setText(QApplication::translate("RobotFootprint", "0.0", nullptr));
        updateButton->setText(QApplication::translate("RobotFootprint", "Update", nullptr));
        refresh_robot->setText(QApplication::translate("RobotFootprint", "Refresh", nullptr));
    } // retranslateUi

};

namespace Ui {
    class RobotFootprint: public Ui_RobotFootprint {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ROBOTFOOTPRINT_H
