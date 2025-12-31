import { useState } from 'react'
import './App.css'
import NewsInput from './components/NewsInput'
import PredictionResult from './components/PredictionResult'

function App() {
  const [prediction, setPrediction] = useState(null)
  const [loading, setLoading] = useState(false)

  const handlePrediction = (result) => {
    setPrediction(result)
    setLoading(false)
  }

  const handleReset = () => {
    setPrediction(null)
  }

  return (
    <div className="glass-container">
      <h1>AI News Classifier</h1>
      <p className="subtitle">Powered by Advanced MLOps Pipeline</p>

      {!prediction ? (
        <NewsInput
          onPrediction={handlePrediction}
          setLoading={setLoading}
          loading={loading}
        />
      ) : (
        <PredictionResult
          result={prediction}
          onReset={handleReset}
        />
      )}
    </div>
  )
}

export default App
