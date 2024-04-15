/********************************************************************************
** Form generated from reading UI file 'robotCreator.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ROBOTCREATOR_H
#define UI_ROBOTCREATOR_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_RobotCreator
{
public:
    QGridLayout *gridLayout_2;
    QGridLayout *gridLayout;
    QVBoxLayout *verticalLayout;
    QTreeWidget *robotTreeWidget;
    QLabel *robotPreviewLabel;
    QFrame *line_3;
    QGridLayout *gridLayout_3;
    QPushButton *loadRobotButton;

    void setupUi(QWidget *RobotCreator)
    {
        if (RobotCreator->objectName().isEmpty())
            RobotCreator->setObjectName(QString::fromUtf8("RobotCreator"));
        RobotCreator->resize(808, 564);
        RobotCreator->setMinimumSize(QSize(808, 564));
        RobotCreator->setMaximumSize(QSize(808, 564));
        gridLayout_2 = new QGridLayout(RobotCreator);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout = new QGridLayout();
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        robotTreeWidget = new QTreeWidget(RobotCreator);
        robotTreeWidget->headerItem()->setText(2, QString());
        robotTreeWidget->headerItem()->setText(3, QString());
        robotTreeWidget->headerItem()->setText(4, QString());
        robotTreeWidget->setObjectName(QString::fromUtf8("robotTreeWidget"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(1);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(robotTreeWidget->sizePolicy().hasHeightForWidth());
        robotTreeWidget->setSizePolicy(sizePolicy);
        robotTreeWidget->setMinimumSize(QSize(300, 0));
        robotTreeWidget->setMaximumSize(QSize(300, 16777210));
        robotTreeWidget->setHorizontalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        robotTreeWidget->setWordWrap(true);
        robotTreeWidget->setColumnCount(5);
        robotTreeWidget->header()->setMinimumSectionSize(10);
        robotTreeWidget->header()->setDefaultSectionSize(20);

        verticalLayout->addWidget(robotTreeWidget);


        gridLayout->addLayout(verticalLayout, 0, 0, 1, 1);

        robotPreviewLabel = new QLabel(RobotCreator);
        robotPreviewLabel->setObjectName(QString::fromUtf8("robotPreviewLabel"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(robotPreviewLabel->sizePolicy().hasHeightForWidth());
        robotPreviewLabel->setSizePolicy(sizePolicy1);
        robotPreviewLabel->setMinimumSize(QSize(480, 480));
        robotPreviewLabel->setMaximumSize(QSize(480, 480));

        gridLayout->addWidget(robotPreviewLabel, 0, 1, 1, 1);


        gridLayout_2->addLayout(gridLayout, 0, 0, 1, 1);

        line_3 = new QFrame(RobotCreator);
        line_3->setObjectName(QString::fromUtf8("line_3"));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);

        gridLayout_2->addWidget(line_3, 1, 0, 1, 1);

        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        gridLayout_3->setSizeConstraint(QLayout::SetDefaultConstraint);
        loadRobotButton = new QPushButton(RobotCreator);
        loadRobotButton->setObjectName(QString::fromUtf8("loadRobotButton"));
        loadRobotButton->setMinimumSize(QSize(150, 0));
        loadRobotButton->setMaximumSize(QSize(150, 16777215));

        gridLayout_3->addWidget(loadRobotButton, 0, 0, 1, 1);


        gridLayout_2->addLayout(gridLayout_3, 2, 0, 1, 1);


        retranslateUi(RobotCreator);

        QMetaObject::connectSlotsByName(RobotCreator);
    } // setupUi

    void retranslateUi(QWidget *RobotCreator)
    {
        RobotCreator->setWindowTitle(QApplication::translate("RobotCreator", "STDR Robot creator", nullptr));
        QTreeWidgetItem *___qtreewidgetitem = robotTreeWidget->headerItem();
        ___qtreewidgetitem->setText(1, QApplication::translate("RobotCreator", "Info", nullptr));
        ___qtreewidgetitem->setText(0, QApplication::translate("RobotCreator", "Robot parts", nullptr));
        robotPreviewLabel->setText(QString());
        loadRobotButton->setText(QApplication::translate("RobotCreator", "Add Robot to map", nullptr));
    } // retranslateUi

};

namespace Ui {
    class RobotCreator: public Ui_RobotCreator {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ROBOTCREATOR_H
