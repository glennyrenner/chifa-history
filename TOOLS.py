from GUI import GUI

class ChifaScrapper:
    def scrape(self, path):
        import os
        batch = []
        for center_folder in os.listdir(path):
            center_path = os.path.join(path, center_folder)
            for bord_folder in os.listdir(center_path):
                bord_path = os.path.join(center_path, bord_folder)
                for file in os.listdir(bord_path):
                    filename = os.path.join(bord_path, file)
                    if filename.endswith('.xml'):
                        try:
                            item = self._scrape_xml(filename)
                            batch.append(item)
                        except Exception as e:
                            print(e)  
        return batch

    def _scrape_xml(self, filename):
        from xml.etree import ElementTree as ET
        tree = ET.parse(filename)
        root = tree.getroot()
        center = root.find("CENTRE").text
        client = root.find("NO_ASSURE").text
        bill = root.find("NO_FACT").text
        date = root.find("DATE_FACT").text
        bord = root.find("NO_BORDEREAU_FACT").text
        paid_by_client = root.find("MT_ASSURE").text
        paid_by_insurance = root.find("MT_OFFICINE").text
        data = {
            'center' : center,
            'client' : client,
            'bill' : bill,
            'date' : date,
            'bord' : bord,
            'mt_client' : paid_by_client,
            'mt_insurance' : paid_by_insurance,
            'mt' : str(float(paid_by_client) + float(paid_by_insurance))
        }
        return data

if __name__ == '__main__':
    scrapper = ChifaScrapper()
    batch = scrapper.scrape("D:\\Chifa\\CHIFA_OFFICINE\\Cnas_Signed_Client")