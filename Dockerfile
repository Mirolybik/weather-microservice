# Используем официальный образ Python  
FROM python:3.11-slim  

# Устанавливаем рабочую директорию  
WORKDIR /app

ENV PYTHONPATH=/app

# Копируем зависимости  
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

# Копируем исходный код  
COPY app/ ./app

# Устанавливаем команду запуска  
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]