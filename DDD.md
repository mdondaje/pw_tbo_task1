# Zadanie 1 - Domain Driven Design

## Opis Zadania

Celem zadania jest zamodelowanie fragmentu systemu bankowego, zgodnie z zasadami Domain Driven Design (DDD). Fragment koncentruje się na zarządzaniu kontem oraz realizacji przelewów. Zakres obejmuje kilka encji, agregaty i obiekty wartości, a także ograniczenia dotyczące ich atrybutów i formatów danych.

## Model Kontekstowy

![Model](model.png)

W naszym projekcie wyodrębniono dwa główne Bounded Contexty:
1. **Zarządzanie Kontem**: Odpowiada za zarządzanie danymi konta bankowego, w tym danymi klienta.
2. **Przelewy**: Obsługuje proces inicjacji i realizacji przelewów między kontami.

### Agregaty, Encje i Obiekty Wartości

#### Agregat: KontoBankowe
- **Encje**:
  - `KontoBankowe`: Reprezentuje konto bankowe klienta z atrybutami, takimi jak numer konta, saldo.
  - `Klient`: Przechowuje informacje o kliencie (np. imię, nazwisko, PESEL).
- **Obiekty Wartości**:
  - `Adres`: Przechowuje adres klienta.
  - `Saldo`: Informacja o saldzie konta, typ Money (np. PLN).

#### Agregat: Przelew
- **Encje**:
  - `Przelew`: Reprezentuje operację przelewu między kontami z atrybutami, takimi jak numer przelewu, kwota przelewu, data.
- **Obiekty Wartości**:
  - `KwotaPrzelewu`: Reprezentuje kwotę przelewu w postaci Money (waluta i kwota).
  
#### Założenia i Ograniczenia
| Encja/Obiekt Wartości | Atrybuty                           | Ograniczenia/Opis                                                                                           |
|---|---|----|
| `KontoBankowe`        | numerKonta, saldo                 | Numer konta jest unikalny; saldo przechowywane jako Money w walucie PLN                                      |
| `Klient`              | imie, nazwisko, PESEL             | PESEL musi być unikalny                                                                                      |
| `Adres`               | ulica, numer, kodPocztowy, miasto | Kod pocztowy musi być w formacie XX-XXX                                                                      |
| `Przelew`             | numerPrzelewu, kwota, data        | Numer przelewu jest unikalny; data przechowywana jako LocalDateTime                                          |
| `KwotaPrzelewu`       | kwota, waluta                     | Waluta przelewu musi być zgodna z walutą konta; kwota przechowywana jako Money                               |
