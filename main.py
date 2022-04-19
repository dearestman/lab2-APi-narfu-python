import requests

BASE_URL = 'http://testruz.agtu.ru/RUZService/RUZService.svc'

def testApi():
    print("Введите дату в формате yyyy.mm.dd")
    fromDate = str(input())
    # 2018.09.03
    endDate = fromDate
    lecturerOid = 24044
    response = requests.get(f"{BASE_URL}/lessons?fromdate={fromDate}&todate={endDate}&lecturerOid={lecturerOid}&receivertype={1}")
    rqst = response.json()
    print(response.text)
    count = 1
    for r in rqst:
        print(f"{count}. Предмет: {r['discipline']}, группа: {r['group']}, "
              f"тип занятия: {r['kindOfWork']}, время начала занятия: {r['beginLesson']}, время конца занятия: {r['endLesson']}")
        count = count + 1






    # responce = requests.get("http://testruz.agtu.ru/RUZService/RUZService.svc/groups?facultyoid=3")
    # responce2 = requests.get("http://testruz.agtu.ru/RUZService/RUZService.svc/lessons?fromdate='2018.09.03'&todate='2018.09.07'&groupoid=8885&lectureroid=0&auditoriumoid=0")
    # responce2 = requests.get("http://testruz.agtu.ru/RUZService/RUZService.svc/lessons?fromdate='2018.09.03'&todate='2018.09.07'&groupoid=8885&lectureroid=0&auditoriumoid=0")
    # print(responce.json()[40])
    # print(responce2.json())

def returnListOfGroup():
    return 0


if __name__ == '__main__':
    testApi()


