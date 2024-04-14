import configparser
import os

def startConfig():
    config = configparser.ConfigParser()
    path = "settings.ini"

    if not os.path.exists(path):
        config = configparser.ConfigParser()
        with open(path, "w") as config_file:
            config.write(config_file)

    config = configparser.ConfigParser()
    config.read("settings.ini")
    try:
        config["SQL"]
    except:
        config.add_section("SQL")
    try:
        config["DB"]
    except:
        config.add_section("DB")
    # try:
    #     config["MQTT"]
    # except:
    #     config.add_section("MQTT")
    try:
        config["APP"]
    except:
        config.add_section("APP")
    try:
        config["ORG"]
    except:
        config.add_section("ORG")

    with open(path, "w") as config_file:
        config.write(config_file)
    try:
        config["SQL"]["user"]
    except:
        config.set("SQL", "user", "")
    try:
        config["SQL"]["password"]
    except:
        config.set("SQL", "password", "")
    try:
        config["SQL"]["host"]
    except:
        config.set("SQL", "host", "")
    try:
        config["SQL"]["port"]
    except:
        config.set("SQL", "port", "")
    try:
        config["SQL"]["database"]
    except:
        config.set("SQL", "database", "")
    try:
        config["DB"]["structsub"]
    except:
        config.set("DB", "structsub", "structsub")
    try:
        config["DB"]["job"]
    except:
        config.set("DB", "job", "job")
    try:
        config["DB"]["type"]
    except:
        config.set("DB", "type", "type")
    try:
        config["DB"]["records"]
    except:
        config.set("DB", "records", "records")
    try:
        config["DB"]["uid"]
    except:
        config.set("DB", "uid", "uid")
    try:
        config["DB"]["user"]
    except:
        config.set("DB", "user", "user")
    try:
        config["DB"]["topic"]
    except:
        config.set("DB", "topic", "topic")
    try:
        config["DB"]["appRole"]
    except:
        config.set("DB", "appRole", "appRole")
    try:
        config["DB"]["userapp"]
    except:
        config.set("DB", "userapp", "userApp")
    try:
        config["DB"]["setuserapp"]
    except:
        config.set("DB", "setuserapp", "setUserApp")
    try:
        config["DB"]["work"]
    except:
        config.set("DB", "work", "work")
    try:
        config["DB"]["organization"]
    except:
        config.set("DB", "organization", "organization")
    try:
        config["DB"]["ref"]
    except:
        config.set("DB", "ref", "ref")
    # try:
    #     config["MQTT"]["broker"]
    # except:
    #     config.set("MQTT", "broker", "")
    # try:
    #     config["MQTT"]["port"]
    # except:
    #     config.set("MQTT", "port", "")
    # try:
    #     config["MQTT"]["username"]
    # except:
    #     config.set("MQTT", "username", "")
    # try:
    #     config["MQTT"]["password"]
    # except:
    #     config.set("MQTT", "password", "")
    # try:
    #     config["MQTT"]["topic_info"]
    # except:
    #     config.set("MQTT", "topic_info", "")
    # try:
    #     config["MQTT"]["mes_info"]
    # except:
    #     config.set("MQTT", "mes_info", "")
    # try:
    #     config["MQTT"]["client_id"]
    # except:
    #     config.set("MQTT", "client_id", "")
    # try:
    #     config["MQTT"]["version"]
    # except:
    #     config.set("MQTT", "version", "5")
    # try:
    #     config["MQTT"]["tcp"]
    # except:
    #     config.set("MQTT", "tcp", "tcp")
    # try:
    #     config["MQTT"]["add"]
    # except:
    #     config.set("MQTT", "add", "")
    # try:
    #     config["MQTT"]["enable"]
    # except:
    #     config.set("MQTT", "enable", "")
    try:
        config["APP"]["login"]
    except:
        config.set("APP", "login", "")
    try:
        config["APP"]["password"]
    except:
        config.set("APP", "password", "")
    try:
        config["APP"]["savepass"]
    except:
        config.set("APP", "savepass", "1")
    try:
        config["ORG"]["orgname"]
    except:
        config.set("ORG", "orgname", "org")

    with open(path, "w") as config_file:
        config.write(config_file)

    # return newset
    # if newset == True:
    #     msgInfoKey('Был изменен конфигурационный файл, для корректной работы рекомендуем перезагрузить программу?')
