import { useState } from "react";

function ChatPage() {
  const mood = localStorage.getItem("mood") || "Not Selected";

  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text: `👋 Hi Mahesh! I noticed you're feeling ${mood} today. I'm here to listen, support and help you make the most of your work experience.`,
    },
  ]);

  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return;

    const userMessage = {
      sender: "user",
      text: input,
    };

    const aiMessage = {
      sender: "ai",
      text: "Thank you for sharing. I understand how you feel. Tell me a little more about it.",
    };

    setMessages((prev) => [...prev, userMessage, aiMessage]);
    setInput("");
  };

  return (
    <div className="min-h-screen bg-slate-100 flex flex-col">

      {/* Header */}
      <div className="bg-white shadow-md p-4 flex justify-between items-center">

        <div>
          <h2 className="text-2xl font-bold text-blue-700">
            WorkBuddy AI
          </h2>

          <p className="text-gray-500">
            Your Workplace Companion
          </p>
        </div>

        <div className="flex items-center gap-3">

          <div className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full font-medium">
            {mood}
          </div>

          <div className="w-12 h-12 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-lg">
            M
          </div>

        </div>

      </div>

      {/* Chat Area */}
      <div className="flex-1 overflow-y-auto p-6 max-w-6xl w-full mx-auto">

        {/* Insight Card */}
        <div className="bg-gradient-to-r from-blue-50 to-indigo-50 p-5 rounded-2xl shadow-sm mb-6">

          <h3 className="font-bold text-lg mb-2">
            ✨ Today's Insight
          </h3>

          <p className="text-gray-600">
            Small consistent efforts lead to meaningful growth.
          </p>

        </div>

        {/* Quick Actions */}
        <div className="flex flex-wrap gap-3 mb-6">

          <button className="bg-white px-4 py-2 rounded-full shadow hover:bg-blue-50">
            Workload
          </button>

          <button className="bg-white px-4 py-2 rounded-full shadow hover:bg-blue-50">
            Team
          </button>

          <button className="bg-white px-4 py-2 rounded-full shadow hover:bg-blue-50">
            Career Growth
          </button>

          <button className="bg-white px-4 py-2 rounded-full shadow hover:bg-blue-50">
            Learning
          </button>

          <button className="bg-white px-4 py-2 rounded-full shadow hover:bg-blue-50">
            Stress
          </button>

        </div>

        {/* Messages */}
        <div className="space-y-4">

          {messages.map((msg, index) => (
            <div
              key={index}
              className={`flex ${
                msg.sender === "user"
                  ? "justify-end"
                  : "justify-start"
              }`}
            >
              <div
                className={`max-w-xl px-5 py-4 rounded-2xl shadow ${
                  msg.sender === "user"
                    ? "bg-blue-600 text-white"
                    : "bg-white text-gray-800"
                }`}
              >
                {msg.text}
              </div>
            </div>
          ))}

        </div>

      </div>

      {/* Input Section */}
      <div className="bg-white border-t p-4">

        <div className="max-w-6xl mx-auto flex gap-2">

          <button className="px-4 text-2xl">
            📎
          </button>

          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Share what's on your mind..."
            className="flex-1 border rounded-full px-5 py-3 outline-none focus:ring-2 focus:ring-blue-500"
          />

          <button className="px-4 text-2xl">
            🎤
          </button>

          <button
            onClick={sendMessage}
            className="bg-blue-600 text-white px-6 rounded-full hover:bg-blue-700"
          >
            Send
          </button>

        </div>

      </div>

    </div>
  );
}

export default ChatPage;