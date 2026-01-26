import pandas as pd
my_file = "C:/Users/dparjaszewski/Downloads/Ocena narzędzia AI do podsumowania dokumentów RFP.(1-3).xlsx"
df = pd.read_excel(my_file)
general_dict = dict()


#Pytania:
for k, v in df.items():
    set_string = str(k)
    general_dict[set_string] = [t for t  in v]

#Liczymy mierniki:

def calculated_satisfaction(question: str):
    positive_values = 0
    neutral_values = 0
    negative_values = 0
    for k, v in general_dict.items():
        if k == question:
            all_values = len(v)
            for t in v:
                # Pozytywne:
                if t > 3:
                    positive_values += 1
                # Neutralne:
                if t == 3:
                    neutral_values += 1
                # Negatywne
                if t < 3:
                    negative_values+=1
                else:
                    continue
            average_amount = round((positive_values / all_values) * 100, 1)
            return (
                   f"Miernik satysfkacji: {average_amount}% \n"
                   f"Liczba zadowolonych użytkowników: {positive_values} z {all_values} \n"
                   f"Liczba neutralnych użytkowników: {neutral_values} z {all_values} \n"
                   f"Liczba niezadowolonych użytkowników: {negative_values} z {all_values}")
        else:
            pass

def calculated_document_summary(question: str):
    positive_values = 0
    neutral_values = 0
    negative_values = 0
    for k, v in general_dict.items():
        if k == question:
            all_values = len(v)
            for t in v:
                # Pozytywne:
                if t > 3:
                    positive_values += 1
                # Neutralne:
                if t == 3:
                    neutral_values += 1
                # Negatywne
                if t < 3:
                    negative_values += 1
                else:
                    continue
            average_amount = round((positive_values / all_values) * 100, 1)
            return (
                f"Miernik podsumowywanych treści: {average_amount}% \n"
                f"Liczba zadowolonych użytkowników: {positive_values} z {all_values} \n"
                f"Liczba neutralnych użytkowników: {neutral_values} z {all_values} \n"
                f"Liczba niezadowolonych użytkowników: {negative_values} z {all_values}")
        else:
            pass

def calculated_recommendations(question: str):
    positive_values = 0
    neutral_values = 0
    negative_values = 0
    for k, v in general_dict.items():
        if k == question:
            all_values = len(v)
            for t in v:
                # Pozytywne:
                if t > 3:
                    positive_values += 1
                # Neutralne:
                if t == 3:
                    neutral_values += 1
                # Negatywne
                if t < 3:
                    negative_values += 1
                else:
                    continue
            average_amount = round((positive_values / all_values) * 100, 1)
            return (
                f"Miernik rekomendowanych treści: {average_amount}% \n"
                f"Liczba zadowolonych użytkowników: {positive_values} z {all_values} \n"
                f"Liczba neutralnych użytkowników: {neutral_values} z {all_values} \n"
                f"Liczba niezadowolonych użytkowników: {negative_values} z {all_values}")
        else:
            pass

def calculated_timesaver(question: str):
    positive_values = 0
    neutral_values = 0
    negative_values = 0
    for k, v in general_dict.items():
        if k == question:
            all_values = len(v)
            for t in v:
                # Pozytywne:
                if t > 3:
                    positive_values += 1
                # Neutralne:
                if t == 3:
                    neutral_values += 1
                # Negatywne
                if t < 3:
                    negative_values +=1
                else:
                    continue
            average_amount = round((positive_values / all_values) * 100, 1)
            return (
                f"Miernik czasu: {average_amount}% \n"
                f"Liczba użytkowników, dla których narzędzie przyspieszyło proces:  {positive_values} z {all_values} \n"
                f"Liczba neutralnych użytkowników: {neutral_values} z {all_values} \n"
                f"Liczba użytkowników, dla których narzędzie opóźnia proces: {negative_values} z {all_values}")
        else:
            pass

def calculated_returns(question: str):
    positive_values = 0
    neutral_values = 0
    negative_values = 0
    for k, v in general_dict.items():
        if k == question:
            all_values = len(v)
            for t in v:
                # Pozytywne:
                if t > 3:
                    positive_values += 1
                # Neutralne:
                if t == 3:
                    neutral_values += 1
                # Negatywne
                if t < 3:
                    negative_values+=1
                else:
                    continue
            average_amount = round((positive_values / all_values) * 100, 1)
            return (
                f"Miernik powrotu do aplikacji: {average_amount}% \n"
                f"Liczba użytkowników, którzy dalej będą korzystać z narzędzia:  {positive_values} z {all_values} \n"
                f"Liczba neutralnych użytkowników: {neutral_values} z {all_values} \n"
                f"Liczba użytkowników, którzy nie będą korzystać z narzędzia: {negative_values} z {all_values}")
        else:
            pass

#Wyniki:
print(calculated_satisfaction('Jak oceniasz swoje ogólne zadowolenie z korzystania z narzędzia?'))
print(" ")
print(calculated_document_summary('Czy narzędzie spełnia Twoje oczekiwania w zakresie podsumowania dokumentów?'))
print(" ")
print(calculated_recommendations('Jak oceniasz trafność i przydatność rekomendacji generowanych przez narzędzie?'))
print(" ")
print(calculated_timesaver('Czy narzędzie pozwala Ci zaoszczędzić czas w pracy?'))
print(" ")
print(calculated_returns('Czy będziesz dalej korzystać z narzędzia w przyszłości? '))





