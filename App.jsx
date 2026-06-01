

import {
  FaHome,
  FaUsers,
  FaBell,
  FaChartLine,
  FaBrain,
  FaUserCircle,
  FaMicrophone,
  FaCamera,
  FaExclamationTriangle
} from "react-icons/fa"

function App() {

  const time = new Date().toLocaleTimeString()

  return (

    <div className="relative flex min-h-screen overflow-hidden bg-gradient-to-br from-slate-900 via-purple-900 to-black text-white">

      {/* Background Glow */}
      <div className="absolute top-0 left-0 w-96 h-96 bg-pink-500 rounded-full blur-3xl opacity-20 animate-pulse"></div>

      <div className="absolute bottom-0 right-0 w-96 h-96 bg-blue-500 rounded-full blur-3xl opacity-20 animate-pulse"></div>

      {/* Sidebar */}
      <div className="w-72 bg-black/40 backdrop-blur-xl p-6 border-r border-white/10 z-10">

        <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-pink-400 to-blue-400 mb-10">

          Emotion AI

        </h1>

        <ul className="space-y-5">

          <li className="bg-white text-black p-4 rounded-2xl flex items-center gap-4 font-bold">

            <FaHome />
            Dashboard

          </li>

          <li className="hover:bg-white hover:text-black p-4 rounded-2xl flex items-center gap-4 cursor-pointer transition">

            <FaUsers />
            Employees

          </li>

          <li className="hover:bg-white hover:text-black p-4 rounded-2xl flex items-center gap-4 cursor-pointer transition">

            <FaChartLine />
            Analytics

          </li>

          <li className="hover:bg-white hover:text-black p-4 rounded-2xl flex items-center gap-4 cursor-pointer transition">

            <FaBrain />
            AI Insights

          </li>

        </ul>

        {/* AI Status */}
        <div className="mt-12 bg-white/10 p-5 rounded-3xl">

          <h2 className="text-2xl font-bold mb-4">

            AI Status 🤖

          </h2>

          <p className="text-green-400 mb-2">

            ● Face Detection Active

          </p>

          <p className="text-blue-400 mb-2">

            ● Voice Analysis Running

          </p>

          <p className="text-pink-400">

            ● Emotion Prediction Enabled

          </p>

        </div>

      </div>

      {/* Main */}
      <div className="flex-1 p-8 z-10">

        {/* Navbar */}
        <div className="bg-white/10 backdrop-blur-xl p-6 rounded-3xl flex justify-between items-center mb-8 border border-white/10">

          <div>

            <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-pink-400">

              Employee Emotion Prediction

            </h1>

            <p className="text-gray-300 mt-2">

              AI powered employee monitoring system

            </p>

          </div>

          <div className="flex items-center gap-5">

            <p className="bg-white/10 px-4 py-2 rounded-2xl">

              {time}

            </p>

            <input
              type="text"
              placeholder="Search employee..."
              className="bg-white/10 border border-white/10 px-5 py-3 rounded-2xl outline-none"
            />

            <div className="relative">

              <FaBell size={24} />

              <span className="absolute -top-2 -right-2 bg-red-500 text-xs px-2 rounded-full">

                3

              </span>

            </div>

            <FaUserCircle size={45} />

          </div>

        </div>

        {/* Employee Selector */}
        <div className="bg-white/10 backdrop-blur-xl p-6 rounded-3xl mb-8 border border-white/10">

          <h2 className="text-2xl font-bold mb-4">

            Select Employee 👨‍💻

          </h2>

          <select className="bg-black/40 p-4 rounded-2xl w-full text-white outline-none">

            <option>Rahul</option>
            <option>Priya</option>
            <option>Arun</option>
            <option>Sneha</option>

          </select>

        </div>

        {/* Main Emotion Cards */}
        <div className="grid grid-cols-4 gap-6 mb-8">

          {/* Emotion */}
          <div className="bg-gradient-to-br from-pink-500 to-red-500 p-6 rounded-3xl shadow-2xl">

            <h3 className="text-xl font-bold">

              Current Emotion

            </h3>

            <p className="text-4xl mt-4 font-extrabold">

              😟 Stressed

            </p>

            <p className="mt-2 text-lg">

              Confidence: 82%

            </p>

          </div>

          {/* Risk */}
          <div className="bg-gradient-to-br from-red-500 to-orange-500 p-6 rounded-3xl shadow-2xl">

            <h3 className="text-xl font-bold">

              Resignation Risk

            </h3>

            <p className="text-5xl mt-4 font-extrabold">

              85%

            </p>

            <p className="mt-2">

              HIGH RISK

            </p>

          </div>

          {/* Productivity */}
          <div className="bg-gradient-to-br from-green-400 to-emerald-600 p-6 rounded-3xl shadow-2xl">

            <h3 className="text-xl font-bold">

              Productivity

            </h3>

            <p className="text-5xl mt-4 font-extrabold">

              72%

            </p>

            <p className="mt-2">

              Moderate

            </p>

          </div>

          {/* Stress */}
          <div className="bg-gradient-to-br from-blue-500 to-indigo-600 p-6 rounded-3xl shadow-2xl">

            <h3 className="text-xl font-bold">

              Stress Level

            </h3>

            <p className="text-5xl mt-4 font-extrabold">

              78%

            </p>

            <p className="mt-2">

              Critical

            </p>

          </div>

        </div>

        {/* Face + Voice */}
        <div className="grid grid-cols-2 gap-6 mb-8">

          {/* Face Recognition */}
          <div className="bg-white/10 backdrop-blur-xl p-8 rounded-3xl border border-white/10">

            <h2 className="text-3xl font-bold mb-6">

              Face Emotion Analysis 🎥

            </h2>

            <div className="h-72 bg-black rounded-3xl flex flex-col items-center justify-center mb-6">

              <FaCamera size={60} className="mb-4 text-cyan-400" />

              <p className="text-2xl font-bold">

                Live Camera Feed

              </p>

            </div>

            <div className="flex items-center gap-5">

              <img
                src="https://i.pravatar.cc/150?img=12"
                className="w-32 h-32 rounded-3xl border-4 border-pink-500"
              />

              <div>

                <p className="text-2xl font-bold">

                  Rahul Detected

                </p>

                <p className="mt-2 text-gray-300">

                  Emotion: Sad 😔

                </p>

                <p className="mt-2 text-red-400 font-bold">

                  Burnout Detected

                </p>

              </div>

            </div>

          </div>

          {/* Voice Analysis */}
          <div className="bg-white/10 backdrop-blur-xl p-8 rounded-3xl border border-white/10">

            <h2 className="text-3xl font-bold mb-6">

              Voice Emotion Analysis 🎤

            </h2>

            <div className="bg-gradient-to-r from-purple-500 to-pink-500 p-6 rounded-3xl mb-6">

              <div className="flex items-center gap-4 mb-4">

                <FaMicrophone size={30} />

                <h3 className="text-2xl font-bold">

                  Voice Input

                </h3>

              </div>

              <p className="text-lg">

                “I feel stressed because of workload”

              </p>

            </div>

            <div className="space-y-4">

              <div className="bg-red-500/20 p-4 rounded-2xl">

                Stress Level: 82%

              </div>

              <div className="bg-yellow-500/20 p-4 rounded-2xl">

                Burnout Risk: High

              </div>

              <div className="bg-blue-500/20 p-4 rounded-2xl">

                Emotion Tone: Negative

              </div>

            </div>

          </div>

        </div>

        {/* Mood Graph */}
        <div className="bg-white/10 backdrop-blur-xl p-8 rounded-3xl mb-8 border border-white/10">

          <h2 className="text-3xl font-bold mb-6">

            Weekly Emotion Trend 📈

          </h2>

          <div className="h-72 bg-gradient-to-r from-blue-500/20 via-pink-500/20 to-purple-500/20 rounded-3xl flex items-center justify-center text-3xl font-bold">

            Emotion Graph Visualization

          </div>

        </div>

        {/* AI Recommendation */}
        <div className="bg-white/10 backdrop-blur-xl p-8 rounded-3xl mb-8 border border-white/10">

          <h2 className="text-3xl font-bold mb-6">

            AI Recommendation 🤖

          </h2>

          <div className="space-y-5">

            <div className="bg-red-500/20 p-5 rounded-2xl flex items-center gap-4">

              <FaExclamationTriangle className="text-red-400" />

              Provide workload reduction for Rahul

            </div>

            <div className="bg-blue-500/20 p-5 rounded-2xl">

              Schedule HR wellness meeting

            </div>

            <div className="bg-green-500/20 p-5 rounded-2xl">

              Encourage team engagement activities

            </div>

          </div>

        </div>

        {/* Employee Table */}
        <div className="bg-white/10 backdrop-blur-xl p-8 rounded-3xl border border-white/10">

          <h2 className="text-3xl font-bold mb-6">

            Employee Emotion Report 📋

          </h2>

          <table className="w-full">

            <thead>

              <tr className="text-left bg-white/10">

                <th className="p-4">Name</th>
                <th className="p-4">Emotion</th>
                <th className="p-4">Risk</th>
                <th className="p-4">Stress</th>

              </tr>

            </thead>

            <tbody>

              <tr className="border-b border-white/10 hover:bg-white/5">

                <td className="p-4">Rahul</td>
                <td className="p-4">😟 Stressed</td>
                <td className="p-4 text-red-400">High</td>
                <td className="p-4">82%</td>

              </tr>

              <tr className="border-b border-white/10 hover:bg-white/5">

                <td className="p-4">Priya</td>
                <td className="p-4">😊 Happy</td>
                <td className="p-4 text-green-400">Low</td>
                <td className="p-4">20%</td>

              </tr>

            </tbody>

          </table>

        </div>

      </div>

    </div>
  )
}

export default App
