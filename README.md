<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Autocom Japan Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        #chatbox { width: 400px; height: 300px; border: 1px solid #ccc; padding: 10px; overflow-y: scroll; margin: auto; }
        #userInput { width: 300px; padding: 5px; }
        button { padding: 5px 10px; }
    </style>
</head>
<body>
    <h2>Autocom Japan Chatbot</h2>
    <div id="chatbox"></div>
    <input type="text" id="userInput" placeholder="Ask me about Autocom Japan...">
    <button onclick="sendMessage()">Send</button>

    <script>
        function sendMessage() {
            let userMessage = document.getElementById("userInput").value;
            if (!userMessage) return;
            document.getElementById("chatbox").innerHTML += `<p><b>You:</b> ${userMessage}</p>`;
            
            fetch("https://your-backend-url/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("chatbox").innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;
            });

            document.getElementById("userInput").value = "";
        }
    </script>
</body>
</html>
