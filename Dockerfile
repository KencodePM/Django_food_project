FROM python:3.10.5-alpine

#複製 requirements.txt進入docker 內部
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#新增資料夾
RUN mkdir /app
#將外部的app資料夾複製進入docker內部
COPY . /app
#設定當前工作環境路徑為 /app
WORKDIR /app

RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]