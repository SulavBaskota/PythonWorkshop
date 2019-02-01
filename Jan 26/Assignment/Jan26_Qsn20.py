"""
Q20. Define a class that does currency conversion. The method you define must convert at least 10
foreign currency to NRP.
"""


class CurrencyConversion:

    @staticmethod
    def usd_to_nrp(rup):
        print(f"{rup} USD = {rup*113.69}")

    @staticmethod
    def yen_to_nrp(rup):
        print(f"{rup} Yen = {rup * 10.44/10}")

    @staticmethod
    def euro_to_nrp(rup):
        print(f"{rup} euro = {rup * 130.44}")

    @staticmethod
    def yuan_to_nrp(rup):
        print(f"{rup} Yuan = {rup * 16.88}")

    @staticmethod
    def aud_to_nrp(rup):
        print(f"{rup} AuD = {rup * 82.56}")

    @staticmethod
    def hkd_to_nrp(rup):
        print(f"{rup} HKD = {rup* 14.49}")

    @staticmethod
    def won_to_nrp(rup):
        print(f"{rup} won = {rup * 10.18 / 100}")

    @staticmethod
    def pound_to_nrp(rup):
        print(f"{rup} pound = {rup *148.57}")

    @staticmethod
    def swiss_to_nrp(rup):
        print(f"{rup} swiss franc = {rup * 114.55}")

    @staticmethod
    def uae_to_nrp(rup):
        print(f"{rup} UAE Dirham = {rup *30.95}")


rups = CurrencyConversion()
rups.aud_to_nrp(1)
rups.euro_to_nrp(1)
rups.hkd_to_nrp(1)
rups.pound_to_nrp(1)
rups.swiss_to_nrp(1)
rups.uae_to_nrp(1)
rups.usd_to_nrp(1)
rups.won_to_nrp(100)
rups.yen_to_nrp(10)
rups.yuan_to_nrp(1)




