
if __name__ == "__main__":
    import csv
    from unittest import TestCase
    import unittest
    
    calls_sum_dict = dict()
    
    
    with open('phoneCalls.csv','r') as fin:
        # csv.DictReader uses first line in file for column headings by default
        reader = csv.reader(fin, delimiter = ",") # comma is default delimiter
        headers = next(reader)
        for row in reader:
            from_subscr = int(row[0])
            if from_subscr not in calls_sum_dict:
                calls_sum_dict[from_subscr] = 0
                # value = int(row[3])
                value =1
                calls_sum_dict[from_subscr] += value
    
    class MenadzerPolaczen:
      def __init__(self, filename):
        self.filename = filename
        self.data_dict = self.read_data()
    
      def read_data(self):
        calls_dict_sum = dict()
        with open(self.filename, 'r') as fin:
          reader = csv.reader(fin, delimiter= ",")
          headers = next(reader)
    
          for row in reader:
            from_subsr = int(row[0])
            if from_subsr not in calls_dict_sum:
              calls_dict_sum[from_subsr] = 0
            calls_dict_sum[from_subsr] += 1
        return calls_dict_sum
    
      def pobierz_najczesciej_dzwoniacego(self):
        return max(self.data_dict.items(), key= lambda x: x[1])
    
    
    class SprawdzDzwoniacegoTest(TestCase):
      def test_czy_abonent_najczesciej_dzwoniacy_rozpoznany_poprawnie(self):
        mp = MenadzerPolaczen("phoneCalls.csv")
        wynik = mp.pobierz_najczesciej_dzwoniacego()
        self.assertEqual((226,5), wynik)
    
    
    #Nasz kod poprawnie przechodzi test jednostkowy
    unittest.main(argv=[''], defaultTest='SprawdzDzwoniacegoTest', exit=False)
    
    
    nazwa_pliku = "phoneCalls.csv"
    mp = MenadzerPolaczen(nazwa_pliku)
    wynik = mp.pobierz_najczesciej_dzwoniacego()
    print(wynik)
    
    
    
    
