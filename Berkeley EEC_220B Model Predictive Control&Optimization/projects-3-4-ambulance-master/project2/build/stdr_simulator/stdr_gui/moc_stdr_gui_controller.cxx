/****************************************************************************
** Meta object code from reading C++ file 'stdr_gui_controller.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.12.8)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../src/stdr_simulator/stdr_gui/include/stdr_gui/stdr_gui_controller.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'stdr_gui_controller.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.12.8. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_stdr_gui__CGuiController_t {
    QByteArrayData data[58];
    char stringdata0[985];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_stdr_gui__CGuiController_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_stdr_gui__CGuiController_t qt_meta_stringdata_stdr_gui__CGuiController = {
    {
QT_MOC_LITERAL(0, 0, 24), // "stdr_gui::CGuiController"
QT_MOC_LITERAL(1, 25, 16), // "waitForRobotPose"
QT_MOC_LITERAL(2, 42, 0), // ""
QT_MOC_LITERAL(3, 43, 18), // "waitForThermalPose"
QT_MOC_LITERAL(4, 62, 14), // "waitForCo2Pose"
QT_MOC_LITERAL(5, 77, 16), // "waitForSoundPose"
QT_MOC_LITERAL(6, 94, 15), // "waitForRfidPose"
QT_MOC_LITERAL(7, 110, 12), // "replaceRobot"
QT_MOC_LITERAL(8, 123, 11), // "std::string"
QT_MOC_LITERAL(9, 135, 12), // "robotFrameId"
QT_MOC_LITERAL(10, 148, 18), // "setLaserVisibility"
QT_MOC_LITERAL(11, 167, 9), // "robotName"
QT_MOC_LITERAL(12, 177, 9), // "laserName"
QT_MOC_LITERAL(13, 187, 2), // "vs"
QT_MOC_LITERAL(14, 190, 18), // "setSonarVisibility"
QT_MOC_LITERAL(15, 209, 9), // "sonarName"
QT_MOC_LITERAL(16, 219, 23), // "setRfidReaderVisibility"
QT_MOC_LITERAL(17, 243, 14), // "rfidReaderName"
QT_MOC_LITERAL(18, 258, 22), // "setCO2SensorVisibility"
QT_MOC_LITERAL(19, 281, 13), // "co2SensorName"
QT_MOC_LITERAL(20, 295, 26), // "setThermalSensorVisibility"
QT_MOC_LITERAL(21, 322, 17), // "thermalSensorName"
QT_MOC_LITERAL(22, 340, 24), // "setSoundSensorVisibility"
QT_MOC_LITERAL(23, 365, 15), // "soundSensorName"
QT_MOC_LITERAL(24, 381, 18), // "setRobotVisibility"
QT_MOC_LITERAL(25, 400, 16), // "saveRobotPressed"
QT_MOC_LITERAL(26, 417, 19), // "stdr_msgs::RobotMsg"
QT_MOC_LITERAL(27, 437, 11), // "newRobotMsg"
QT_MOC_LITERAL(28, 449, 9), // "file_name"
QT_MOC_LITERAL(29, 459, 16), // "loadRobotPressed"
QT_MOC_LITERAL(30, 476, 24), // "loadRobotFromFilePressed"
QT_MOC_LITERAL(31, 501, 15), // "loadRfidPressed"
QT_MOC_LITERAL(32, 517, 14), // "loadCo2Pressed"
QT_MOC_LITERAL(33, 532, 16), // "loadSoundPressed"
QT_MOC_LITERAL(34, 549, 18), // "loadThermalPressed"
QT_MOC_LITERAL(35, 568, 13), // "zoomInPressed"
QT_MOC_LITERAL(36, 582, 1), // "p"
QT_MOC_LITERAL(37, 584, 14), // "zoomOutPressed"
QT_MOC_LITERAL(38, 599, 13), // "robotPlaceSet"
QT_MOC_LITERAL(39, 613, 12), // "rfidPlaceSet"
QT_MOC_LITERAL(40, 626, 15), // "thermalPlaceSet"
QT_MOC_LITERAL(41, 642, 11), // "co2PlaceSet"
QT_MOC_LITERAL(42, 654, 13), // "soundPlaceSet"
QT_MOC_LITERAL(43, 668, 17), // "updateMapInternal"
QT_MOC_LITERAL(44, 686, 22), // "laserVisualizerClicked"
QT_MOC_LITERAL(45, 709, 22), // "sonarVisualizerClicked"
QT_MOC_LITERAL(46, 732, 22), // "robotVisualizerClicked"
QT_MOC_LITERAL(47, 755, 11), // "itemClicked"
QT_MOC_LITERAL(48, 767, 15), // "Qt::MouseButton"
QT_MOC_LITERAL(49, 783, 1), // "b"
QT_MOC_LITERAL(50, 785, 15), // "robotReplaceSet"
QT_MOC_LITERAL(51, 801, 22), // "laserVisibilityClicked"
QT_MOC_LITERAL(52, 824, 22), // "sonarVisibilityClicked"
QT_MOC_LITERAL(53, 847, 27), // "rfidReaderVisibilityClicked"
QT_MOC_LITERAL(54, 875, 26), // "co2SensorVisibilityClicked"
QT_MOC_LITERAL(55, 902, 30), // "thermalSensorVisibilityClicked"
QT_MOC_LITERAL(56, 933, 28), // "soundSensorVisibilityClicked"
QT_MOC_LITERAL(57, 962, 22) // "robotVisibilityClicked"

    },
    "stdr_gui::CGuiController\0waitForRobotPose\0"
    "\0waitForThermalPose\0waitForCo2Pose\0"
    "waitForSoundPose\0waitForRfidPose\0"
    "replaceRobot\0std::string\0robotFrameId\0"
    "setLaserVisibility\0robotName\0laserName\0"
    "vs\0setSonarVisibility\0sonarName\0"
    "setRfidReaderVisibility\0rfidReaderName\0"
    "setCO2SensorVisibility\0co2SensorName\0"
    "setThermalSensorVisibility\0thermalSensorName\0"
    "setSoundSensorVisibility\0soundSensorName\0"
    "setRobotVisibility\0saveRobotPressed\0"
    "stdr_msgs::RobotMsg\0newRobotMsg\0"
    "file_name\0loadRobotPressed\0"
    "loadRobotFromFilePressed\0loadRfidPressed\0"
    "loadCo2Pressed\0loadSoundPressed\0"
    "loadThermalPressed\0zoomInPressed\0p\0"
    "zoomOutPressed\0robotPlaceSet\0rfidPlaceSet\0"
    "thermalPlaceSet\0co2PlaceSet\0soundPlaceSet\0"
    "updateMapInternal\0laserVisualizerClicked\0"
    "sonarVisualizerClicked\0robotVisualizerClicked\0"
    "itemClicked\0Qt::MouseButton\0b\0"
    "robotReplaceSet\0laserVisibilityClicked\0"
    "sonarVisibilityClicked\0"
    "rfidReaderVisibilityClicked\0"
    "co2SensorVisibilityClicked\0"
    "thermalSensorVisibilityClicked\0"
    "soundSensorVisibilityClicked\0"
    "robotVisibilityClicked"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_stdr_gui__CGuiController[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      40,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
      13,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,  214,    2, 0x06 /* Public */,
       3,    0,  215,    2, 0x06 /* Public */,
       4,    0,  216,    2, 0x06 /* Public */,
       5,    0,  217,    2, 0x06 /* Public */,
       6,    0,  218,    2, 0x06 /* Public */,
       7,    1,  219,    2, 0x06 /* Public */,
      10,    3,  222,    2, 0x06 /* Public */,
      14,    3,  229,    2, 0x06 /* Public */,
      16,    3,  236,    2, 0x06 /* Public */,
      18,    3,  243,    2, 0x06 /* Public */,
      20,    3,  250,    2, 0x06 /* Public */,
      22,    3,  257,    2, 0x06 /* Public */,
      24,    2,  264,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      25,    2,  269,    2, 0x0a /* Public */,
      29,    1,  274,    2, 0x0a /* Public */,
      30,    1,  277,    2, 0x0a /* Public */,
      31,    0,  280,    2, 0x0a /* Public */,
      32,    0,  281,    2, 0x0a /* Public */,
      33,    0,  282,    2, 0x0a /* Public */,
      34,    0,  283,    2, 0x0a /* Public */,
      35,    1,  284,    2, 0x0a /* Public */,
      37,    1,  287,    2, 0x0a /* Public */,
      38,    1,  290,    2, 0x0a /* Public */,
      39,    1,  293,    2, 0x0a /* Public */,
      40,    1,  296,    2, 0x0a /* Public */,
      41,    1,  299,    2, 0x0a /* Public */,
      42,    1,  302,    2, 0x0a /* Public */,
      43,    0,  305,    2, 0x0a /* Public */,
      44,    2,  306,    2, 0x0a /* Public */,
      45,    2,  311,    2, 0x0a /* Public */,
      46,    1,  316,    2, 0x0a /* Public */,
      47,    2,  319,    2, 0x0a /* Public */,
      50,    2,  324,    2, 0x0a /* Public */,
      51,    2,  329,    2, 0x0a /* Public */,
      52,    2,  334,    2, 0x0a /* Public */,
      53,    2,  339,    2, 0x0a /* Public */,
      54,    2,  344,    2, 0x0a /* Public */,
      55,    2,  349,    2, 0x0a /* Public */,
      56,    2,  354,    2, 0x0a /* Public */,
      57,    1,  359,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, 0x80000000 | 8,    9,
    QMetaType::Void, QMetaType::QString, QMetaType::QString, QMetaType::Char,   11,   12,   13,
    QMetaType::Void, QMetaType::QString, QMetaType::QString, QMetaType::Char,   11,   15,   13,
    QMetaType::Void, QMetaType::QString, QMetaType::QString, QMetaType::Char,   11,   17,   13,
    QMetaType::Void, QMetaType::QString, QMetaType::QString, QMetaType::Char,   11,   19,   13,
    QMetaType::Void, QMetaType::QString, QMetaType::QString, QMetaType::Char,   11,   21,   13,
    QMetaType::Void, QMetaType::QString, QMetaType::QString, QMetaType::Char,   11,   23,   13,
    QMetaType::Void, QMetaType::QString, QMetaType::Char,   11,   13,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 26, QMetaType::QString,   27,   28,
    QMetaType::Void, 0x80000000 | 26,   27,
    QMetaType::Void, 0x80000000 | 26,   27,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QPoint,   36,
    QMetaType::Void, QMetaType::QPoint,   36,
    QMetaType::Void, QMetaType::QPoint,   36,
    QMetaType::Void, QMetaType::QPoint,   36,
    QMetaType::Void, QMetaType::QPoint,   36,
    QMetaType::Void, QMetaType::QPoint,   36,
    QMetaType::Void, QMetaType::QPoint,   36,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,   11,   12,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,   11,   15,
    QMetaType::Void, QMetaType::QString,   11,
    QMetaType::Void, QMetaType::QPoint, 0x80000000 | 48,   36,   49,
    QMetaType::Void, QMetaType::QPoint, 0x80000000 | 8,   36,   11,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,   11,   12,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,   11,   15,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,   11,   17,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,   11,   19,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,   11,   21,
    QMetaType::Void, QMetaType::QString, QMetaType::QString,   11,   23,
    QMetaType::Void, QMetaType::QString,   11,

       0        // eod
};

void stdr_gui::CGuiController::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<CGuiController *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->waitForRobotPose(); break;
        case 1: _t->waitForThermalPose(); break;
        case 2: _t->waitForCo2Pose(); break;
        case 3: _t->waitForSoundPose(); break;
        case 4: _t->waitForRfidPose(); break;
        case 5: _t->replaceRobot((*reinterpret_cast< std::string(*)>(_a[1]))); break;
        case 6: _t->setLaserVisibility((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< char(*)>(_a[3]))); break;
        case 7: _t->setSonarVisibility((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< char(*)>(_a[3]))); break;
        case 8: _t->setRfidReaderVisibility((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< char(*)>(_a[3]))); break;
        case 9: _t->setCO2SensorVisibility((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< char(*)>(_a[3]))); break;
        case 10: _t->setThermalSensorVisibility((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< char(*)>(_a[3]))); break;
        case 11: _t->setSoundSensorVisibility((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2])),(*reinterpret_cast< char(*)>(_a[3]))); break;
        case 12: _t->setRobotVisibility((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< char(*)>(_a[2]))); break;
        case 13: _t->saveRobotPressed((*reinterpret_cast< stdr_msgs::RobotMsg(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 14: _t->loadRobotPressed((*reinterpret_cast< stdr_msgs::RobotMsg(*)>(_a[1]))); break;
        case 15: _t->loadRobotFromFilePressed((*reinterpret_cast< stdr_msgs::RobotMsg(*)>(_a[1]))); break;
        case 16: _t->loadRfidPressed(); break;
        case 17: _t->loadCo2Pressed(); break;
        case 18: _t->loadSoundPressed(); break;
        case 19: _t->loadThermalPressed(); break;
        case 20: _t->zoomInPressed((*reinterpret_cast< QPoint(*)>(_a[1]))); break;
        case 21: _t->zoomOutPressed((*reinterpret_cast< QPoint(*)>(_a[1]))); break;
        case 22: _t->robotPlaceSet((*reinterpret_cast< QPoint(*)>(_a[1]))); break;
        case 23: _t->rfidPlaceSet((*reinterpret_cast< QPoint(*)>(_a[1]))); break;
        case 24: _t->thermalPlaceSet((*reinterpret_cast< QPoint(*)>(_a[1]))); break;
        case 25: _t->co2PlaceSet((*reinterpret_cast< QPoint(*)>(_a[1]))); break;
        case 26: _t->soundPlaceSet((*reinterpret_cast< QPoint(*)>(_a[1]))); break;
        case 27: _t->updateMapInternal(); break;
        case 28: _t->laserVisualizerClicked((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 29: _t->sonarVisualizerClicked((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 30: _t->robotVisualizerClicked((*reinterpret_cast< QString(*)>(_a[1]))); break;
        case 31: _t->itemClicked((*reinterpret_cast< QPoint(*)>(_a[1])),(*reinterpret_cast< Qt::MouseButton(*)>(_a[2]))); break;
        case 32: _t->robotReplaceSet((*reinterpret_cast< QPoint(*)>(_a[1])),(*reinterpret_cast< std::string(*)>(_a[2]))); break;
        case 33: _t->laserVisibilityClicked((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 34: _t->sonarVisibilityClicked((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 35: _t->rfidReaderVisibilityClicked((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 36: _t->co2SensorVisibilityClicked((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 37: _t->thermalSensorVisibilityClicked((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 38: _t->soundSensorVisibilityClicked((*reinterpret_cast< QString(*)>(_a[1])),(*reinterpret_cast< QString(*)>(_a[2]))); break;
        case 39: _t->robotVisibilityClicked((*reinterpret_cast< QString(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (CGuiController::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::waitForRobotPose)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::waitForThermalPose)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::waitForCo2Pose)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::waitForSoundPose)) {
                *result = 3;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::waitForRfidPose)) {
                *result = 4;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)(std::string );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::replaceRobot)) {
                *result = 5;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)(QString , QString , char );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::setLaserVisibility)) {
                *result = 6;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)(QString , QString , char );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::setSonarVisibility)) {
                *result = 7;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)(QString , QString , char );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::setRfidReaderVisibility)) {
                *result = 8;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)(QString , QString , char );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::setCO2SensorVisibility)) {
                *result = 9;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)(QString , QString , char );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::setThermalSensorVisibility)) {
                *result = 10;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)(QString , QString , char );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::setSoundSensorVisibility)) {
                *result = 11;
                return;
            }
        }
        {
            using _t = void (CGuiController::*)(QString , char );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CGuiController::setRobotVisibility)) {
                *result = 12;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject stdr_gui::CGuiController::staticMetaObject = { {
    &QThread::staticMetaObject,
    qt_meta_stringdata_stdr_gui__CGuiController.data,
    qt_meta_data_stdr_gui__CGuiController,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *stdr_gui::CGuiController::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *stdr_gui::CGuiController::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_stdr_gui__CGuiController.stringdata0))
        return static_cast<void*>(this);
    return QThread::qt_metacast(_clname);
}

int stdr_gui::CGuiController::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QThread::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 40)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 40;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 40)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 40;
    }
    return _id;
}

// SIGNAL 0
void stdr_gui::CGuiController::waitForRobotPose()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void stdr_gui::CGuiController::waitForThermalPose()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void stdr_gui::CGuiController::waitForCo2Pose()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void stdr_gui::CGuiController::waitForSoundPose()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void stdr_gui::CGuiController::waitForRfidPose()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void stdr_gui::CGuiController::replaceRobot(std::string _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 5, _a);
}

// SIGNAL 6
void stdr_gui::CGuiController::setLaserVisibility(QString _t1, QString _t2, char _t3)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)), const_cast<void*>(reinterpret_cast<const void*>(&_t3)) };
    QMetaObject::activate(this, &staticMetaObject, 6, _a);
}

// SIGNAL 7
void stdr_gui::CGuiController::setSonarVisibility(QString _t1, QString _t2, char _t3)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)), const_cast<void*>(reinterpret_cast<const void*>(&_t3)) };
    QMetaObject::activate(this, &staticMetaObject, 7, _a);
}

// SIGNAL 8
void stdr_gui::CGuiController::setRfidReaderVisibility(QString _t1, QString _t2, char _t3)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)), const_cast<void*>(reinterpret_cast<const void*>(&_t3)) };
    QMetaObject::activate(this, &staticMetaObject, 8, _a);
}

// SIGNAL 9
void stdr_gui::CGuiController::setCO2SensorVisibility(QString _t1, QString _t2, char _t3)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)), const_cast<void*>(reinterpret_cast<const void*>(&_t3)) };
    QMetaObject::activate(this, &staticMetaObject, 9, _a);
}

// SIGNAL 10
void stdr_gui::CGuiController::setThermalSensorVisibility(QString _t1, QString _t2, char _t3)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)), const_cast<void*>(reinterpret_cast<const void*>(&_t3)) };
    QMetaObject::activate(this, &staticMetaObject, 10, _a);
}

// SIGNAL 11
void stdr_gui::CGuiController::setSoundSensorVisibility(QString _t1, QString _t2, char _t3)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)), const_cast<void*>(reinterpret_cast<const void*>(&_t3)) };
    QMetaObject::activate(this, &staticMetaObject, 11, _a);
}

// SIGNAL 12
void stdr_gui::CGuiController::setRobotVisibility(QString _t1, char _t2)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)), const_cast<void*>(reinterpret_cast<const void*>(&_t2)) };
    QMetaObject::activate(this, &staticMetaObject, 12, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
