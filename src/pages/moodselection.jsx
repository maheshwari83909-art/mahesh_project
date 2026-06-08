import { useState } from "react";
import { useNavigate } from "react-router-dom";

function MoodSelection() {
  const navigate = useNavigate();
  const [selectedMood, setSelectedMood] = useState("");

 const moods = [
  { emoji: "🚀", mood: "Motivated" },
  { emoji: "⚡", mood: "Energized" },
  { emoji: "🎯", mood: "Focused" },
  { emoji: "🤝", mood: "Connected" },
  { emoji: "😓", mood: "Overwhelmed" },
  { emoji: "😣", mood: "Stressed" },
 ];

  const handleSubmit = () => {
    localStorage.setItem("mood", selectedMood);
    navigate("/chat");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 p-8">

      <div className="max-w-5xl mx-auto">

        <div className="text-center mb-12">

          <h1 className="text-5xl font-bold text-gray-800 mb-4">
            Let's Check In
          </h1>

          <p className="text-gray-500 text-lg">
            Take a moment to share how you're feeling today.
          </p>

        </div>

        <div className="grid md:grid-cols-3 gap-6">

          {moods.map((item) => (
            <div
              key={item.mood}
              onClick={() => setSelectedMood(item.mood)}
              className={`cursor-pointer rounded-3xl p-8 text-center bg-white shadow-lg hover:shadow-2xl hover:-translate-y-2 transition-all duration-300
              ${
                selectedMood === item.mood
                  ? "ring-4 ring-blue-500 bg-blue-50"
                  : ""
              }`}
            >
              <div className="text-6xl mb-4">
                {item.emoji}
              </div>

              <h2 className="text-2xl font-semibold text-gray-800">
                {item.mood}
              </h2>

            </div>
          ))}

        </div>

        <div className="text-center mt-12">

          <button
            onClick={handleSubmit}
            disabled={!selectedMood}
            className="bg-blue-600 text-white px-12 py-4 rounded-full text-lg font-semibold hover:bg-blue-700 transition disabled:opacity-50"
          >
            Let's Get Started →
          </button>

        </div>

      </div>

    </div>
  );
}

export default MoodSelection;