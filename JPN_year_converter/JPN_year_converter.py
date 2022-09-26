import re
import unicodedata
import sys

class JPN_year_converter:
    def __init__(self) -> None:
        self.wareki_era = {"明治": 1868, "大正": 1912, "昭和": 1926, "平成": 1989, "令和": 2019}
        self.wareki_initial = {"明治": "M", "大正": "T", "昭和": "S", "平成": "H", "令和": "R"}

    def ADYear2warekiYear(self, AD_year:int,kanji:bool=False,gan_nen=True)->str:
        """
        Convert a AD year to Wareki year
        
        Params:
        ---
        AD_year: int
            Year
        kanji: bool
            If you want to get a value in Japanese(Kanji), please set True
        gan_nen: bool
            Which you want to express the first year of Japanese era, "元年" or "1年 ?
            Note: If you set "kanji" variable to False, this variable does not work.

        Return:
        ---
        Waraki(Japanese era):str
        """
        def calc_Wareki_from_AD(wareki_era:str):
            wareki_year_calc:str = str(int(AD_year - self.wareki_era[wareki_era]+1))
            if not kanji:
                return self.wareki_initial[wareki_era] + wareki_year_calc
            if kanji and gan_nen and wareki_year_calc == "1":
                return wareki_era+"元年度"
            if kanji:
                return wareki_era+wareki_year_calc+"年度"
                
        if AD_year<self.wareki_era["明治"]:
            print('Error: Wareki may be invalid values.\n We have supported eras which are after Meiji(1868).', file=sys.stderr)
            sys.exit(1)

        if AD_year>=self.wareki_era["令和"]:
            return calc_Wareki_from_AD("令和")
        if AD_year>=self.wareki_era["平成"]:
            return calc_Wareki_from_AD("平成")
        if AD_year>=self.wareki_era["昭和"]:
            return calc_Wareki_from_AD("昭和")
        if AD_year>=self.wareki_era["大正"]:
            return calc_Wareki_from_AD("大正")
        if AD_year>=self.wareki_era["明治"]:
            return calc_Wareki_from_AD("明治")
        

    def warekiYear2ADYear(self, wareki:str):
        """Convert a Wareki year to AD year"""
        def calc_AD_from_Wareki(era:str):
            return self.wareki_era[era] + number_year - 1

        if type(wareki)!=str:
            return None
        wareki_normalized=unicodedata.normalize('NFKC',wareki)
        
        number_year_re=re.search(pattern="[0-9]{1,2}|元",string=wareki_normalized)
        if number_year_re is None:
            print('Error: Cannot convert the Wareki to AD year!', file=sys.stderr)
            sys.exit(1)
        if number_year_re.group(0) == "元":
            number_year = 1
        else:
            number_year = int(number_year_re.group(0))
        
        if re.search(pattern="^(R|r|令和|れいわ|レイワ)",string=wareki_normalized):
            return calc_AD_from_Wareki("令和")
        if re.search(pattern="^(H|h|平成|へいせい|ヘイセイ)",string=wareki_normalized):
            return calc_AD_from_Wareki("平成")
        if re.search(pattern="^(S|s|昭和|しょうわ|ショウワ)",string=wareki_normalized):
            return calc_AD_from_Wareki("昭和")
        if re.search(pattern="^(T|t|大正|たいしょう|タイショウ)",string=wareki_normalized):
            return calc_AD_from_Wareki("大正")
        if re.search(pattern="^(M|m|明治|めいじ|メイジ)",string=wareki_normalized):
            return calc_AD_from_Wareki("明治")
        
        print('Error: Wareki may be invalid values.\n We have supported eras which are after Meiji(明治).', file=sys.stderr)
        sys.exit(1)