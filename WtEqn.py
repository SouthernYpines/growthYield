class GreenWeight:
    '''
    This class contains methods to calculate green weight of loblolly, slash, and longleaf in lbs
    '''
    def __init__(self, dbh, height, mtop):
        # Initialize object attributes
        self.dbh = dbh
        self.height = height
        self.mtop = mtop
 
    def slashGreenWt(self):
        return(0)
    def lobGreenWt(self, location):
        if location.lower() == "lcp":
            return(0.0740959 * self.dbh**1.829983 * self.height**1.247669 - 0.123329 *(self.mtop**3.523107 / self.dbh**1.449947) * (self.height-4.5))
        elif location.lower() == "ucp":
            return(0.141534 * self.dbh**1.917146 * self.height**1.038452 - 0.0932063 * (self.mtop**3.589155 / self.dbh**1.413061) * (self.height-4.5))
        elif location.lower() == "piedmont" or location.lower()=="pied":
            return(0)
        else:
            return(0)
    def longleafGreenWt(self):
        V4_longleaf = -0.84281 + 0.00216 * self.dbh ** 2 * self.height
        V5_longleaf = V4_longleaf * (1 - 0.682125 * (5 ** 4.543282 / self.dbh ** 4.369255))
        Coef_longleaf = (0.00545415 * (self.mtop ** 2 + 4 ** 2) / 2 * (4 - self.mtop)) * (1 / (0.00545415 * ((4 ** 2 + 5 ** 2) / 2)))
        WT_4_longleaf = -36.83043 + 0.15608 * self.dbh ** 2 * self.height
        if self.mtop > 4:
           return(WT_4_longleaf * (1 - 0.647787 * (self.mTop ^ 4.321359 / self.dbh ^ 4.122653)))
        else:
            return(WT_4_longleaf * (1+ Coef_longleaf * ((V4_longleaf - V5_longleaf)/V4_longleaf)))
        
longleaf = GreenWeight(10, 60, 4)
loblolly = GreenWeight(10,60,4)
print(loblolly.lobGreenWt("lcp"))
print(loblolly.lobGreenWt("ucp"))
print(longleaf.longleafGreenWt())