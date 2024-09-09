def leer_palabras_archivo(file_path, size):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            palabras = [line.strip() for line in file.readlines()]
            return palabras[:size]
    except Exception as e:
        print(f"Error leyendo el archivo: {e}")
        return []

