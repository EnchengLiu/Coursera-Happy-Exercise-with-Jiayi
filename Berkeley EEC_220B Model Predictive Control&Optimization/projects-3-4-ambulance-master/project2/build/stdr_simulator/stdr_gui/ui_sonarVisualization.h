/********************************************************************************
** Form generated from reading UI file 'sonarVisualization.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SONARVISUALIZATION_H
#define UI_SONARVISUALIZATION_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_sonarVisualization
{
public:
    QProgressBar *sonarDistBar;
    QLabel *sonarDist;
    QLabel *sonarMaxDist;
    QLabel *sonarMinDist;

    void setupUi(QWidget *sonarVisualization)
    {
        if (sonarVisualization->objectName().isEmpty())
            sonarVisualization->setObjectName(QString::fromUtf8("sonarVisualization"));
        sonarVisualization->resize(313, 65);
        sonarDistBar = new QProgressBar(sonarVisualization);
        sonarDistBar->setObjectName(QString::fromUtf8("sonarDistBar"));
        sonarDistBar->setGeometry(QRect(10, 10, 291, 21));
        sonarDistBar->setMaximum(1000);
        sonarDistBar->setValue(0);
        sonarDistBar->setTextVisible(true);
        sonarDist = new QLabel(sonarVisualization);
        sonarDist->setObjectName(QString::fromUtf8("sonarDist"));
        sonarDist->setGeometry(QRect(50, 40, 211, 20));
        sonarDist->setFrameShape(QFrame::StyledPanel);
        sonarDist->setFrameShadow(QFrame::Plain);
        sonarDist->setTextFormat(Qt::AutoText);
        sonarDist->setAlignment(Qt::AlignCenter);
        sonarMaxDist = new QLabel(sonarVisualization);
        sonarMaxDist->setObjectName(QString::fromUtf8("sonarMaxDist"));
        sonarMaxDist->setGeometry(QRect(260, 40, 51, 20));
        sonarMaxDist->setFrameShape(QFrame::StyledPanel);
        sonarMaxDist->setFrameShadow(QFrame::Plain);
        sonarMaxDist->setTextFormat(Qt::AutoText);
        sonarMaxDist->setAlignment(Qt::AlignCenter);
        sonarMinDist = new QLabel(sonarVisualization);
        sonarMinDist->setObjectName(QString::fromUtf8("sonarMinDist"));
        sonarMinDist->setGeometry(QRect(0, 40, 51, 20));
        sonarMinDist->setFrameShape(QFrame::StyledPanel);
        sonarMinDist->setFrameShadow(QFrame::Plain);
        sonarMinDist->setTextFormat(Qt::AutoText);
        sonarMinDist->setAlignment(Qt::AlignCenter);

        retranslateUi(sonarVisualization);

        QMetaObject::connectSlotsByName(sonarVisualization);
    } // setupUi

    void retranslateUi(QWidget *sonarVisualization)
    {
        sonarVisualization->setWindowTitle(QApplication::translate("sonarVisualization", "Form", nullptr));
        sonarDistBar->setFormat(QString());
        sonarDist->setText(QApplication::translate("sonarVisualization", "0 m", nullptr));
        sonarMaxDist->setText(QApplication::translate("sonarVisualization", "0 m", nullptr));
        sonarMinDist->setText(QApplication::translate("sonarVisualization", "0 m", nullptr));
    } // retranslateUi

};

namespace Ui {
    class sonarVisualization: public Ui_sonarVisualization {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SONARVISUALIZATION_H
