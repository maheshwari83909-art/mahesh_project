import { useNavigate } from "react-router-dom";

function JourneyGate() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 to-slate-700 flex justify-center items-center px-4">

      <div className="text-center text-white max-w-2xl">

        <h1 className="text-6xl font-bold mb-6">
          WorkBuddy AI
        </h1>

        <p className="text-xl text-gray-300 mb-10">
          This space is designed to understand,
          support and empower you throughout
          your work experience.
        </p>

        <button
          onClick={() => navigate("/chat")}
          className="bg-white text-black px-10 py-4 rounded-full text-lg font-semibold hover:scale-105 transition"
        >
          Let's Get Started →
        </button>

      </div>
    </div>
  );
}

export default JourneyGate;