import { useState } from 'react'
import { classifyText } from '../api'

const NewsInput = ({ onPrediction, setLoading, loading }) => {
    const [text, setText] = useState("")

    const handleSubmit = async () => {
        if (!text) return;
        setLoading(true);
        try {
            const result = await classifyText(text);
            onPrediction(result);
        } catch (e) {
            alert("Error classifying text");
            setLoading(false);
        }
    }

    return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', width: '100%' }}>
            <textarea
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Paste your article text here to classify..."
                style={{
                    width: '100%',
                    height: '250px',
                    background: 'rgba(0, 0, 0, 0.3)',
                    border: '1px solid var(--primary)',
                    borderRadius: '16px',
                    color: 'white',
                    padding: '1.5rem',
                    fontSize: '1.1rem',
                    fontFamily: 'inherit',
                    resize: 'none',
                    outline: 'none',
                    boxShadow: '0 0 15px rgba(0, 243, 255, 0.05)',
                    transition: 'all 0.3s ease',
                    boxSizing: 'border-box'
                }}
                onFocus={(e) => e.target.style.boxShadow = '0 0 25px rgba(0, 243, 255, 0.2)'}
                onBlur={(e) => e.target.style.boxShadow = '0 0 15px rgba(0, 243, 255, 0.05)'}
            />
            <button
                onClick={handleSubmit}
                disabled={loading}
                style={{
                    padding: '1.2rem 3rem',
                    background: 'linear-gradient(90deg, var(--primary), var(--secondary))',
                    border: 'none',
                    borderRadius: '50px',
                    fontSize: '1.2rem',
                    fontWeight: '800',
                    cursor: loading ? 'wait' : 'pointer',
                    color: 'white',
                    textTransform: 'uppercase',
                    letterSpacing: '1px',
                    boxShadow: '0 0 30px rgba(188, 19, 254, 0.4)',
                    transition: 'transform 0.2s ease, box-shadow 0.2s ease',
                    alignSelf: 'center',
                    minWidth: '200px'
                }}
                onMouseOver={(e) => !loading && (e.target.style.transform = 'scale(1.05)')}
                onMouseOut={(e) => !loading && (e.target.style.transform = 'scale(1)')}
            >
                {loading ? 'Analyzing...' : 'Classify News'}
            </button>
        </div>
    )
}
export default NewsInput
