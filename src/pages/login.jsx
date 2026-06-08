import { useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 via-blue-50 to-indigo-100 flex items-center justify-center px-6">

      <div className="grid md:grid-cols-2 bg-white shadow-2xl rounded-3xl overflow-hidden max-w-5xl w-full">

        {/* Left Section */}
        <div className="bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-12 flex flex-col justify-center">

          <h1 className="text-5xl font-bold mb-6">
            WorkBuddy AI
          </h1>

          <p className="text-xl mb-6 text-blue-100">
            Because every employee deserves
            to be heard, supported and valued.
          </p>

          <div className="text-8xl">
            🤝
          </div>

        </div>

        {/* Right Section */}
        <div className="p-12 flex flex-col justify-center">

          <h2 className="text-3xl font-bold text-gray-800 mb-2">
            Welcome Back
          </h2>

          <p className="text-gray-500 mb-8">
            Sign in to continue your journey.
          </p>

          <div className="space-y-4">

            <input
              type="text"
              placeholder="Employee ID"
              className="w-full p-4 rounded-xl border border-gray-300 outline-none focus:ring-2 focus:ring-blue-500"
            />

            <input
              type="password"
              placeholder="Password"
              className="w-full p-4 rounded-xl border border-gray-300 outline-none focus:ring-2 focus:ring-blue-500"
            />

            <button
              onClick={() => navigate("/welcome")}
              className="w-full bg-blue-600 text-white font-semibold py-4 rounded-xl hover:bg-blue-700 transition"
            >
              Sign In
            </button>

          </div>

        </div>

      </div>

    </div>
  );
}

export default Login;