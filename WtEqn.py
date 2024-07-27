import math
class GreenWeight:
    """
    This class contains methods to calculate green weight of loblolly, slash, and longleaf in lbs.
    """

    LOB_COEFFICIENTS = {
        'lcp': (0.0740959, 1.829983, 1.247669, -0.123329, 3.523107, 1.449947),
        'ucp': (0.141534, 1.917146, 1.038452, -0.0932063, 3.589155, 1.413061),
        'piedmont': (0.110069, 1.935455, 1.080621, -0.0775771, 3.439954, 1.178473),
        'pied': (0.110069, 1.935455, 1.080621, -0.0775771, 3.439954, 1.178473),
        'nla':(-1.9005 ,    2.0023, 0.99208,      2.0576, 2.5644,     3.1028),
        'texas':(-1.9005 ,    2.0023, 0.99208,      2.0576, 2.5644,     3.1028),
        'louisiana':(-1.9005 ,    2.0023, 0.99208,      2.0576, 2.5644,     3.1028)
    }
    
    

    def __init__(self, dbh, height, mtop):
        """
        Initialize object attributes.
        
        Parameters:
        dbh (float): Diameter at breast height
        height (float): Height of the tree
        mtop (float): Diameter at the top of the merchantable stem
        """
        self.dbh = dbh
        self.height = height
        self.mtop = mtop

    def slash_green_weight(self):
        """
        Calculate green weight for slash pine.
        
        Returns:
        float: Green weight in lbs (currently returns 0 as calculation logic is not provided)
        """
        return (0.1763 * self.dbh**1.9604 * self.height**0.9761 - (0.1167* (self.mtop**3.6422 / self.dbh**1.5441) *(self.height - 4.5)))

    def loblolly_green_weight(self, location):
        """
        Calculate green weight for loblolly pine based on location.
        
        Parameters:
        location (str): The location (e.g., "LCP", "UCP", "Piedmont","NLA")
        
        Returns:
        float: Green weight in lbs
        """
        location = location.lower()
        if location in {"lcp","ucp","pied","piedmont"}:
            a, b, c, d, e, f = self.LOB_COEFFICIENTS[location]
            return a * self.dbh ** b * self.height ** c + d * (self.mtop ** e / self.dbh ** f) * (self.height - 4.5)
        elif location in {"texas", "nla","louisiana"}:
            a, b, c, d, e, f = self.LOB_COEFFICIENTS[location]
            return (math.exp((a + b * math.log(self.dbh) + c * math.log(self.height))) * (1 - (d * (self.mtop** e / self.dbh** f))))
        else:
            raise ValueError("Invalid location. Accepted values are 'LCP', 'UCP', 'Piedmont', 'Pied', 'NLA', 'Texas', or 'Louisiana'.")

    def longleaf_green_weight(self):
        """
        Calculate green weight for longleaf pine.
        
        Returns:
        float: Green weight in lbs
        """
        V4_longleaf = -0.84281 + 0.00216 * self.dbh ** 2 * self.height
        V5_longleaf = V4_longleaf * (1 - 0.682125 * (5 ** 4.543282 / self.dbh ** 4.369255))
        coef_longleaf = (0.00545415 * (self.mtop ** 2 + 4 ** 2) / 2 * (4 - self.mtop)) * (1 / (0.00545415 * ((4 ** 2 + 5 ** 2) / 2)))
        wt_4_longleaf = -36.83043 + 0.15608 * self.dbh ** 2 * self.height
        
        if self.mtop > 4:
            return wt_4_longleaf * (1 - 0.647787 * (self.mtop ** 4.321359 / self.dbh ** 4.122653))
        else:
            return wt_4_longleaf * (1 + coef_longleaf * ((V4_longleaf - V5_longleaf) / V4_longleaf))

longleaf = GreenWeight(10, 60, 4)
loblolly = GreenWeight(10,60,4)
slash = GreenWeight(10,60,4)
print(loblolly.loblolly_green_weight("lcp"))
print(loblolly.loblolly_green_weight("ucp"))
print(loblolly.loblolly_green_weight("pied"))
print(loblolly.loblolly_green_weight("nla"))
print(longleaf.longleaf_green_weight())
print(slash.slash_green_weight())