# CSS004

## Készítette

* Szerző: Sallai András
* Copyright © 2014, Sallai András
* Szerkesztve: 2014-2024
* Licenc: CC BY-SA 4.0
* Web: https://szit.hu

## Feladat leírása

Ez a projekt egy weboldal létrehozásáról szól, amely a házi verébről ad információkat. A feladatban szereplő HTML és CSS fájlokat kell létrehozni, valamint a kódot ellenőrizni a megfelelő stílusbeállításokkal. Az oldalon különböző szövegek, címek és bekezdések találhatók, amelyeket a feladatokban megadott módon kell formázni.

## Feladat

1. **HTML fájl:**
   - Az oldal nyelve legyen magyar.
   - A karakterkódolás legyen `UTF-8`.
   - Csatolj egy külső CSS fájlt.
   - A fejezetcímek legyenek megfelelően formázva.
   
2. **CSS fájl:**
   - A `.container` osztálynak 15%-os margót kell adni.
   - A fejezetcímek szövege legyen `navy` színű.
   - A bekezdések sorkizárt módon jelenjenek meg.
   - A főcím legyen középre igazítva.

3. **Tesztelés:**
   - A projekt tartalmazza a `pytest` teszteket, amelyek biztosítják, hogy a HTML és CSS fájlok megfelelnek a feladatban megadott kritériumoknak.

## Fájlok

1. **index.html**: A fő HTML fájl, amely tartalmazza az oldal struktúráját.
2. **style.css**: A külső CSS fájl, amely tartalmazza a stílusbeállításokat.
3. **test_script.py**: A `pytest` tesztfájl, amely ellenőrzi a HTML és CSS fájlokat.

## Tesztelés

A teszteket a következő módon futtathatja:

1. Telepítse a `pytest`-et:

   ```bash
   pip install pytest
