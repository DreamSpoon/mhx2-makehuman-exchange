# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Authors:             Thomas Larsson
#  Script copyright (C) Thomas Larsson 2014
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

from .flags import *
from .rig_joints import *

Joints = [
    ("sternum-0",           "v", 1528),
    ("sternum",             "l", ((0.8, "sternum-0"), (0.2, "neck"))),

    ("l-clav-4",            "vl", ((0.6, 8077), (0.4, 8237))),
    ("l-clav-1",            "l", ((0.75, "l-clavicle"), (0.25, "l-clav-4"))),
    ("l-clav-2",            "l", ((0.5, "l-clavicle"), (0.5, "l-clav-4"))),
    ("l-clav-3",            "l", ((0.25, "l-clavicle"), (0.75, "l-clav-4"))),

    ("r-clav-4",            "vl", ((0.6, 1385), (0.4, 1559))),
    ("r-clav-1",            "l", ((0.75, "r-clavicle"), (0.25, "r-clav-4"))),
    ("r-clav-2",            "l", ((0.5, "r-clavicle"), (0.5, "r-clav-4"))),
    ("r-clav-3",            "l", ((0.25, "r-clavicle"), (0.75, "r-clav-4"))),

    ("l-upper-arm",         "vl", ((0.5, 8121), (0.5, 8361))),
    ("l-deltoid-1",         "vl", ((0.5, 8077), (0.5, 8243))),
    ("l-deltoid-2",         "vl", ((0.5, 8320), (0.5, 8347))),

    ("r-upper-arm",         "vl", ((0.5, 1433), (0.5, 1689))),
    ("r-deltoid-1",         "vl", ((0.5, 1385), (0.5, 1565))),
    ("r-deltoid-2",         "vl", ((0.5, 1648), (0.5, 1675))),

    ("l-serratus-ik",       "l", ((-0.5, "l-serratus-1"), (1.5, "l-serratus-2"))),
    ("r-serratus-ik",       "l", ((-0.5, "r-serratus-1"), (1.5, "r-serratus-2"))),
    ("l-scap-ik-pole",      "o", ("sternum", (0.5,2.0,0))),
    ("l-scap-aim",          "l", ((0.8, "l-clav-4"), (0.2, "neck"))),

    ("r-serratus-ik",       "l", ((-0.5, "r-serratus-1"), (1.5, "r-serratus-2"))),
    ("r-serratus-ik",       "l", ((-0.5, "r-serratus-1"), (1.5, "r-serratus-2"))),
    ("r-scap-ik-pole",      "o", ("sternum", (0.5,2.0,0))),
    ("r-scap-aim",          "l", ((0.8, "r-clav-4"), (0.2, "neck"))),

    ("l-scapula-1",         "vl", ((0.05, 8215), (0.95, 8263))),
    ("l-scapula-2",         "vl", ((0.2, 8073), (0.8, 10442))),

    ("r-scapula-1",         "vl", ((0.05, 1535), (0.95, 1585))),
    ("r-scapula-2",         "vl", ((0.2, 1381), (0.8, 3775))),

    ("l-elbow-tip",         "v", 10058),
    ("r-elbow-tip",         "v", 3390),

    ("l-elbow",             "n", ("l-elbow-raw", "l-upper-arm", "l-elbow-tip", "l-hand")),
    ("r-elbow",             "n", ("r-elbow-raw", "r-shoulder", "r-elbow-tip", "r-hand")),

    ("l-forearm-1",         "l", ((0.75, "l-elbow"), (0.25, "l-hand"))),
    ("r-forearm-1",         "l", ((0.75, "r-elbow"), (0.25, "r-hand"))),

    ("l-wrist-top",         "v", 10548),
    ("l-hand-end",          "v", 9944),

    ("r-wrist-top",         "v", 3883),
    ("r-hand-end",          "v", 3276),
]


HeadsTails = {
    "DEF-sternum" :             ("neck", "sternum"),

    "clavicle.L" :          ("l-clavicle", "l-clav-4"),
    "scapAim.L" :           ("l-clav-4", "l-scap-aim"),
    "DEF-scapula.L" :       ("l-scapula-1", "l-scapula-2"),
    "DEF-serratusIk.L" :    ("l-serratus-ik", ("l-serratus-ik", ysmall)),

    "clavicle.R" :          ("r-clavicle", "r-clav-4"),
    "scapAim.R" :           ("r-clav-4", "r-scap-aim"),
    "DEF-scapula.R" :       ("r-scapula-1", "r-scapula-2"),
    "DEF-serratusIk.R" :    ("r-serratus-ik", ("r-serratus-ik", ysmall)),

    #"loc_shoulder.L" :      ("l-upper-arm", ("l-upper-arm", ysmall)),
    #"deltoidBend.L" :       (("l-deltoid-1", (-0.4,0,0)), "l-deltoid-1"),
    "DEF-deltoid.L" :        ("l-deltoid-1", "l-deltoid-2"),
    "shoulderIk.L" :         ("l-deltoid-2", ("l-deltoid-2", ysmall)),

    #"loc_shoulder.R" :      ("r-upper-arm", ("r-upper-arm", ysmall)),
    #"deltoidBend.R" :       (("r-deltoid-1", (0.4,0,0)), "r-deltoid-1"),
    "DEF-deltoid.R" :           ("r-deltoid-1", "r-deltoid-2"),
    "shoulderIk.R" :        ("r-deltoid-2", ("r-deltoid-2", ysmall)),

    "upper_arm.L" :         ("l-upper-arm", "l-elbow"),
    "forearm.L" :           ("l-elbow", "l-hand"),
    "elbow.fan.L" :         ("l-elbow", "l-forearm-1"),
    "hand.L" :              ("l-hand", "l-hand-end"),

    "upper_arm.R" :         ("r-shoulder", "r-elbow"),
    "forearm.R" :           ("r-elbow", "r-hand"),
    "elbow.fan.R" :         ("r-elbow", "r-forearm-1"),
    "hand.R" :              ("r-hand", "r-hand-end"),

}

Planes = {
    "PlaneArm.L" :         ('l-upper-arm', 'l-elbow-tip', 'l-hand'),
    "PlaneHand.L" :        ('l-plane-hand-1', 'l-plane-hand-2', 'l-plane-hand-3'),
    "PlaneArm.R" :         ('r-shoulder', 'r-elbow-tip', 'r-hand'),
    "PlaneHand.R" :        ('r-plane-hand-1', 'r-plane-hand-2', 'r-plane-hand-3'),
}

Armature = {
    "DEF-sternum" :         (0, "chest-1", F_DEF|F_CON, L_DEF),

    "clavicle.L" :          (0, "chest-1", F_DEF, L_LARMFK|L_LARMIK),
    "scapAim.L" :           (0, "clavicle.L", 0, L_HELP),
    "DEF-scapula.L" :       (0, "scapAim.L", F_DEF, L_DEF),

    "clavicle.R" :          (0, "chest-1", F_DEF, L_RARMFK|L_RARMIK),
    "scapAim.R" :           (0, "clavicle.R", 0, L_HELP),
    "DEF-scapula.R" :       (0, "scapAim.R", F_DEF, L_DEF),

    "DEF-deltoid.L" :       (0, "clavicle.L", F_DEF, L_DEF),
    "DEF-deltoid.R" :       (0, "clavicle.R", F_DEF, L_DEF),

    "pectIk.L" :            (0, "clavicle.L", 0, L_HELP),
    "pectIk.R" :            (0, "clavicle.R", 0, L_HELP),

    "upper_arm.L" :         ("PlaneArm.L", "clavicle.L", F_DEF, L_LARMFK),
    "shoulderIk.L" :        (0, "upper_arm.L", 0, L_HELP),
    "DEF-serratusIk.L" :    (0, "upper_arm.L", 0, L_HELP),
    "forearm.L" :           ("PlaneArm.L", "upper_arm.L", F_DEF|F_CON, L_LARMFK, P_YZX),
    "hand.L" :              ("PlaneHand.L", "forearm.L", F_DEF|F_CON, L_LARMFK, P_YZX),

    "upper_arm.R" :         ("PlaneArm.R", "clavicle.R", F_DEF, L_RARMFK),
    "shoulderIk.R" :        (0, "upper_arm.R", 0, L_HELP),
    "DEF-serratusIk.R" :    (0, "upper_arm.R", 0, L_HELP),
    "forearm.R" :           ("PlaneArm.R", "upper_arm.R", F_DEF|F_CON, L_RARMFK, P_YZX),
    "hand.R" :              ("PlaneHand.R", "forearm.R", F_DEF|F_CON, L_RARMFK, P_YZX),

    "elbow.fan.L" :         ("PlaneArm.L", "upper_arm.L", F_DEF|F_CON, L_DEF, P_YZX),
    "elbow.fan.R" :         ("PlaneArm.R", "upper_arm.R", F_DEF|F_CON, L_DEF, P_YZX),
}


RotationLimits = {
}

CustomShapes = {
    "clavicle.L" :      "GZM_Shoulder",
    "clavicle.R" :      "GZM_Shoulder",
    "upper_arm.L" :     "GZM_Circle025",
    "upper_arm.R" :     "GZM_Circle025",
    "forearm.L" :       "GZM_Circle025",
    "forearm.R" :       "GZM_Circle025",
    "hand.L" :          "GZM_Hand",
    "hand.R" :          "GZM_Hand",
}

clavInf = 0.4

Constraints = {
    "DEF-sternum" : [("CopyRot", C_LOCAL, 0.2, ["neck", "neck", (1,0,0), (0,0,0), False])],

    "DEF-deltoid.L" : [
        ("IK", 0, 1, ["shoulderIk.L", "shoulderIk.L", 1, None, (1,0,1)])
        ],

    "DEF-deltoid.R" : [
        ("IK", 0, 1, ["shoulderIk.R", "shoulderIk.R", 1, None, (1,0,1)])
        ],

    "scapAim.L" : [
        ("IK", 0, 1, ["sternum", "DEF-sternum", 1, None, (1,0,1)])
        ],

    "scapAim.R" : [
        ("IK", 0, 1, ["sternum", "DEF-sternum", 1, None, (1,0,1)])
        ],

    "elbow.fan.L" : [
        ("CopyRot", C_LOCAL, 0.75, ["forearm.L", "forearm.L", (1,1,1), (0,0,0), False])
        ],

    "elbow.fan.R" : [
        ("CopyRot", C_LOCAL, 0.75, ["forearm.R", "forearm.R", (1,1,1), (0,0,0), False])
        ],

}
'''
    "DEF-clav-0.L" : [("CopyRot", C_LOCAL, clavInf, ["clavicle.L", "clavicle.L", (1,1,1), (0,0,0), False])],
    "DEF-clav-1.L" : [("CopyRot", C_LOCAL, clavInf, ["clavicle.L", "clavicle.L", (1,1,1), (0,0,0), False])],
    "DEF-clav-2.L" : [("CopyRot", C_LOCAL, clavInf, ["clavicle.L", "clavicle.L", (1,1,1), (0,0,0), False])],
    "DEF-clav-3.L" : [("CopyRot", C_LOCAL, clavInf, ["clavicle.L", "clavicle.L", (1,1,1), (0,0,0), False])],

    "DEF-clav-0.R" : [("CopyRot", C_LOCAL, clavInf, ["clavicle.R", "clavicle.R", (1,1,1), (0,0,0), False])],
    "DEF-clav-1.R" : [("CopyRot", C_LOCAL, clavInf, ["clavicle.R", "clavicle.R", (1,1,1), (0,0,0), False])],
    "DEF-clav-2.R" : [("CopyRot", C_LOCAL, clavInf, ["clavicle.R", "clavicle.R", (1,1,1), (0,0,0), False])],
    "DEF-clav-3.R" : [("CopyRot", C_LOCAL, clavInf, ["clavicle.R", "clavicle.R", (1,1,1), (0,0,0), False])],
'''
