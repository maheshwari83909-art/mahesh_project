import { useNavigate } from "react-router-dom";

function Welcome() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-sky-100 via-white to-indigo-100 flex items-center justify-center px-4">

      <div className="bg-white shadow-2xl rounded-3xl p-12 max-w-2xl text-center">

        <div className="text-6xl mb-5">👋</div>

        <h1 className="text-5xl font-bold text-gray-800 mb-4">
          Welcome to WorkBuddy AI
        </h1>

        <p className="text-gray-600 text-xl leading-relaxed mb-10 max-w-xl mx-auto">
          We're glad you're here.
        </p>

        <p className="text-gray-600 text-xl leading-relaxed mb-10 max-w-xl mx-auto">
            This space is designed to understand,
            support and empower you throughout
            your work experience.
        </p>

        <button
            onClick={() => navigate("/mood")}
            className="bg-blue-600 text-white px-10 py-4 rounded-full text-lg font-semibold hover:scale-105 transition"
        >
            Continue
        </button>

      </div>

    </div>
  );
}

export default Welcome;