import json

## Code in order to manipulate the NVD JSON feeds in order to create a scikitread_json(-learn friendly CSV

def read_json(file_path):
    # Opens the JSON and retuns it in a python friendly format
    
    json_file = open(file_path)
    data = json.load(json_file)

    return data

def CVE_info(CVE_number, data):
    # Given a CVE number, extracts useful information for machine learning from the database
    # Returns the information in an array

    info_arr = []

    # CVE ID, will be the index
    info_arr.append(data["CVE_Items"][CVE_number]["cve"]["CVE_data_meta"]["ID"])

      # baseMetricV2
    try:
        baseMetric = CVEs["CVE_Items"][CVE_number]["impact"]["baseMetricV2"]

        for item in baseMetric:
            if item == "cvssV2":
                for attribute in baseMetric[item]:
                    if (attribute != "version") and (attribute != "vectorString"):
                        info_arr.append(baseMetric[item][attribute])
                        # print(attribute) -- Commented for debugging and useful for manually creating CSV header
            else:
                info_arr.append(baseMetric[item]) 
                # print(item) -- Commented for debugging and useful for manually creating CSV header
    except KeyError:
        pass



    # # baseMetricV3
    # try:
    #     baseMetric = CVEs["CVE_Items"][CVE_number]["impact"]["baseMetricV3"]

    #     for item in baseMetric:
    #         if item == "cvssV3":
    #             for attribute in baseMetric[item]:
    #                 if (attribute != "version") and (attribute != "vectorString"):
    #                     info_arr.append(baseMetric[item][attribute])
    #                     # print(attribute) -- Commented for debugging and useful for manually creating CSV header
    #         else:
    #             info_arr.append(baseMetric[item])
    #             # print(item) -- Commented for debugging and useful for manually creating CSV header
    # except KeyError:
    #     pass

  
    return info_arr

def append_CSV(data, destination):
    # Appends to a CSV with a pre-existing header
    # Use python NVD_to_CSV.py >> test.csv

    number_entries = data["CVE_data_numberOfCVEs"]

    for i in range(int(number_entries)):
        info_list = CVE_info(i, CVEs)
        string = ",".join(map(str, info_list)) 
        print(string, file=open(destination, "a"))


# Melhorar para não ser hardcoded

# baseMetricV2
header = "ID,accessVector,accessComplexityauthenticationconfidentialityImpact,integrityImpact,availabilityImpact,baseScore,severity,exploitabilityScore,impactScore,obtainAllPrivilege,obtainUserPrivilege,obtainOtherPrivilege,userInteractionRequired"

# baseMetricV3
# header = "ID,attackComplexity,attackVector,availabilityImpact,baseSeverity,userInteraction,baseScore,privilegesRequired,confidentialityImpact,integrityImpact,scope,impactScore,exploitabilityScore"


# Melhorar para ser customizável
destination = "baseMetricV2.csv"
print(header, file=open(destination, "w"))

CVEs = read_json("./data/NVD/nvdcve-1.0-2002.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2003.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2004.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2005.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2006.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2007.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2008.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2009.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2010.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2011.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2012.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2013.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2014.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2015.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2016.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2017.json")
append_CSV(CVEs, destination)

CVEs = read_json("./data/NVD/nvdcve-1.0-2018.json")
append_CSV(CVEs, destination)
