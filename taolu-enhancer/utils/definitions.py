class Joints:
    NUI_SKELETON_POSITION_HIP_CENTER = 0
    NUI_SKELETON_POSITION_SPINE = 1
    NUI_SKELETON_POSITION_SHOULDER_CENTER = 2
    NUI_SKELETON_POSITION_HEAD = 3
    NUI_SKELETON_POSITION_SHOULDER_LEFT = 4
    NUI_SKELETON_POSITION_ELBOW_LEFT = 5
    NUI_SKELETON_POSITION_WRIST_LEFT = 6
    NUI_SKELETON_POSITION_HAND_LEFT = 7
    NUI_SKELETON_POSITION_SHOULDER_RIGHT = 8
    NUI_SKELETON_POSITION_ELBOW_RIGHT = 9
    NUI_SKELETON_POSITION_WRIST_RIGHT = 10
    NUI_SKELETON_POSITION_HAND_RIGHT = 11
    NUI_SKELETON_POSITION_HIP_LEFT = 12
    NUI_SKELETON_POSITION_KNEE_LEFT = 13
    NUI_SKELETON_POSITION_ANKLE_LEFT = 14
    NUI_SKELETON_POSITION_FOOT_LEFT = 15
    NUI_SKELETON_POSITION_HIP_RIGHT = 16
    NUI_SKELETON_POSITION_KNEE_RIGHT = 17
    NUI_SKELETON_POSITION_ANKLE_RIGHT = 18
    NUI_SKELETON_POSITION_FOOT_RIGHT = 19

class Projections:
    ANGLE_NECK_TORSO = 1
    ANGLE_SHOULDER_ARM_R = 2
    ANGLE_SHOULDER_ARM_L = 3
    ANGLE_ARM_ARM_R = 4
    ANGLE_ARM_ARM_L = 5
    ANGLE_HIP_LEG_R = 6
    ANGLE_HIP_LEG_L = 7
    ANGLE_LEG_LEG_R = 8
    ANGLE_LEG_LEG_L = 9
    ANGLE_ARM_HIPLINE_R = 10
    ANGLE_ARM_HIPLINE_L = 11
    ANGLE_THIGH_HIPLINE_R = 12
    ANGLE_THIGH_HIPLINE_L = 13

class Form:
    forms ={"lohan quan p1" : {"m0" : "Preparation",
                    "m1" : "Arhat workships Budha",
                    "m2" : "Separate palm horse",
                    "m3" : "Strike the heart with fist",
                    "m4" : "Arhat restrains tiger",
                    "m5" : "Arhat holds seat",
                    "m6" : "Brush hand and thrust fist in bow stance",
                    "m7" : "Snap kick and thrust fist",
                    "m8" : "Thrust fist in bow stance",
                    "m9" : "Twist body and thrust fist in rest stance",
                    "m10" : "Parry and punch in horse stance",
                    "m11" : "Trowel eyebrow and kick with heel",
                    "m12" : "Step back and push palm twice",
                    "m13" : "Insert first down in T-stance",
                    "m14" : "Tiger-tail foot",
                    "m15" : "Chop and kick",
                    "m16" : "Arhat sleep"},
            "form2":{"m0":"preparation",
                    "m1":"movimiento1"},
            "prueba":{
                    "m1" : "De pie 1",
                    "m2" : "De pie 2",
                    "m3" : "De pie 3",
                    "m4" : "De pie 4",
                    "m5" : "De pie 5",
                    "m6" : "De pie 6",
                    "m7" : "De pie 7",
                    "m8" : "De pie 8",
                    "m9" : "De pie 9",
                    "m10" : "De pie 10",
                    "m11" : "Mano derecha arriba 1",
                    "m12" : "Mano derecha arriba 2",
                    "m13" : "Mano derecha arriba 3",
                    "m14" : "Mano derecha arriba 4",
                    "m15" : "Mano derecha arriba 5",
                    "m16" : "Mano derecha arriba 6",
                    "m17" : "Mano derecha arriba 7",
                    "m18" : "Mano derecha arriba 8",
                    "m19" : "Mano derecha arriba 9",
                    "m20" : "Mano derecha arriba 10",
                    "m21" : "Mano izquierda arriba 1",
                    "m22" : "Mano izquierda arriba 2",
                    "m23" : "Mano izquierda arriba 3",
                    "m24" : "Mano izquierda arriba 4",
                    "m25" : "Mano izquierda arriba 5",
                    "m26" : "Mano izquierda arriba 6",
                    "m27" : "Mano izquierda arriba 7",
                    "m28" : "Mano izquierda arriba 8",
                    "m29" : "Mano izquierda arriba 9",
                    "m30" : "Mano izquierda arriba 10",
                    "m31" : "Posicion de caballo 1",
                    "m32" : "Posicion de caballo 2",
                    "m33" : "Posicion de caballo 3",
                    "m34" : "Posicion de caballo 4",
                    "m35" : "Posicion de caballo 5",
                    "m36" : "Posicion de caballo 6",
                    "m37" : "Posicion de caballo 7",
                    "m38" : "Posicion de caballo 8",
                    "m39" : "Posicion de caballo 9",
                    "m40" : "Posicion de caballo 10",
                    "m41" : "Posicion de vacio lateral 1",
                    "m42" : "Posicion de vacio lateral 2",
                    "m43" : "Posicion de vacio lateral 3",
                    "m44" : "Posicion de vacio lateral 4",
                    "m45" : "Posicion de vacio lateral 5",
                    "m46" : "Posicion de vacio lateral 6",
                    "m47" : "Posicion de vacio lateral 7",
                    "m48" : "Posicion de vacio lateral 8",
                    "m49" : "Posicion de vacio lateral 9",
                    "m50" : "Posicion de vacio lateral 10",
                    
                    },
            }

    abbreviations = {"lohan quan p1" : {"m0" : "P",
                                "m1" : "AWB",
                                "m2" : "SPH",
                                "m3" : "STHWF",
                                "m4" : "ART",
                                "m5" : "AHS",
                                "m6" : "BHATFIBS",
                                "m7" : "SKATF",
                                "m8" : "TFIBS",
                                "m9" : "TBATFIRS",
                                "m10" : "PAPIHS",
                                "m11" : "TEAKWH",
                                "m12" : "SBAPPT",
                                "m13" : "IFDIT",
                                "m14" : "TF",
                                "m15" : "CAK",
                                "m16" : "AS"},
                    "form2":{"m0":"preparation",
                            "m1":"move1"},
                            "prueba":{
                    "m1" : "Depie1",
                    "m2" : "Depie2",
                    "m3" : "Depie3",
                    "m4" : "Depie4",
                    "m5" : "Depie5",
                    "m6" : "Depie6",
                    "m7" : "Depie7",
                    "m8" : "Depie8",
                    "m9" : "Depie9",
                    "m10" : "Depie10",
                    "m11" : "Manoderechaarriba1",
                    "m12" : "Manoderechaarriba2",
                    "m13" : "Manoderechaarriba3",
                    "m14" : "Manoderechaarriba4",
                    "m15" : "Manoderechaarriba5",
                    "m16" : "Manoderechaarriba6",
                    "m17" : "Manoderechaarriba7",
                    "m18" : "Manoderechaarriba8",
                    "m19" : "Manoderechaarriba9",
                    "m20" : "Manoderechaarriba10",
                    "m21" : "Manoizquierdaarriba1",
                    "m22" : "Manoizquierdaarriba2",
                    "m23" : "Manoizquierdaarriba3",
                    "m24" : "Manoizquierdaarriba4",
                    "m25" : "Manoizquierdaarriba5",
                    "m26" : "Manoizquierdaarriba6",
                    "m27" : "Manoizquierdaarriba7",
                    "m28" : "Manoizquierdaarriba8",
                    "m29" : "Manoizquierdaarriba9",
                    "m30" : "Manoizquierdaarriba10",
                    "m31" : "Posiciondecaballo1",
                    "m32" : "Posiciondecaballo2",
                    "m33" : "Posiciondecaballo3",
                    "m34" : "Posiciondecaballo4",
                    "m35" : "Posiciondecaballo5",
                    "m36" : "Posiciondecaballo6",
                    "m37" : "Posiciondecaballo7",
                    "m38" : "Posiciondecaballo8",
                    "m39" : "Posiciondecaballo9",
                    "m40" : "Posiciondecaballo10",
                    "m41" : "Posiciondevaciolateral1",
                    "m42" : "Posiciondevaciolateral2",
                    "m43" : "Posiciondevaciolateral3",
                    "m44" : "Posiciondevaciolateral4",
                    "m45" : "Posiciondevaciolateral5",
                    "m46" : "Posiciondevaciolateral6",
                    "m47" : "Posiciondevaciolateral7",
                    "m48" : "Posiciondevaciolateral8",
                    "m49" : "Posiciondevaciolateral9",
                    "m50" : "Posiciondevaciolateral10",
                    },
    }

    