var socket;
const express = require("express");
const app = express();
const port = 3000;

const { Kafka } = require("kafkajs");

const kafka = new Kafka({
  clientId: "my-app",
  brokers: ["localhost:9092"],
});

const producer = kafka.producer();

const initKafka = async () => {
  await producer.connect();
};

app.get("/send", async (req, res) => {
  await producer.send({
    topic: "test-topic",
    messages: [{ value: req.params("text") }],
  });
  res.send("successfully stored event : " + req.params("text") + "\n");
});

app.listen(port, async () => {
  console.log(`kafka app listening on port ${port}`);
});

initKafka();

// $("#text").keypress(function (e) {
//   var code = e.keyCode || e.which;
//   if (code == 13) {
//     text = $("#text").val();
//     $("#text").val("");
//     socket.emit("text", { msg: text });
//   }
// });
// 클라이언트는 텍스트를 입력하고 엔터를 쳤을 때, 서버에게 해당 내용은 전송하는 코드가 아래처럼 포함되어 있는 걸 알 수 있다.
