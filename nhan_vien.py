class Nhan_Vien():
    __ma_nhan_vien = ""
    __ten_nhan_vien = ""
    __chuc_vu = ""

    def __init__(self, ma = "", ten = "", chuc_vu = ""):
        self.__ma_nhan_vien = ma
        self.__ten_nhan_vien = ten
        self.__chuc_vu = chuc_vu

    def get_ma_nhan_vien(self):
        return self.__ma_nhan_vien

    def get_ten_nhan_vien(self):
        return self.__ten_nhan_vien

    def get_chuc_vu(self):
        return self.__chuc_vu
