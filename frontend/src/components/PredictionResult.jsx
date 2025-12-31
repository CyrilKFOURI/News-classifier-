import React from 'react'

const PredictionResult = ({ result, onReset }) => {
    return (
        <div style={{ animation: 'fadeIn 0.8s ease' }}>
            <h2 style={{ 
                color: 'var(--text-muted)', 
                textTransform: 'uppercase', 
                letterSpacing: '2px', 
                fontSize: '0.9rem',
                marginBottom: '1rem' 
            }}>
                Detected Category
            </h2>
            
            <div style={{ 
                fontSize: '4rem', 
                fontWeight: '900', 
                background: 'linear-gradient(to right, #fff, var(--primary))',
                -webkit-background-clip: 'text',
                backgroundClip: 'text',
                color: 'transparent',
                marginBottom: '1.5rem',
                filter: 'drop-shadow(0 0 10px rgba(0,243,255,0.5))'
            }}>
                {result.category}
            </div>
            
            <div style={{ 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center', 
                gap: '1rem', 
                marginBottom: '3rem',
                fontSize: '1.2rem',
                background: 'rgba(255,255,255,0.05)',
                padding: '0.5rem 1.5rem',
                borderRadius: '50px',
                width: 'fit-content',
                margin: '0 auto 3rem auto'
            }}>
                <span>Confidence:</span>
                <span style={{ 
                    color: 'var(--success)', 
                    fontWeight: 'bold',
                    textShadow: '0 0 10px rgba(0, 255, 157, 0.5)'
                }}>
                    {(result.confidence * 100).toFixed(1)}%
                </span>
            </div>

            <button 
                onClick={onReset}
                style={{
                    background: 'transparent',
                    border: '1px solid var(--text-muted)',
                    color: 'var(--text-muted)',
                    padding: '0.8rem 2rem',
                    borderRadius: '20px',
                    cursor: 'pointer',
                    fontSize: '0.9rem',
                    transition: 'all 0.3s ease'
                }}
                onMouseOver={(e) => {
                    e.target.style.borderColor = 'white';
                    e.target.style.color = 'white';
                }}
                onMouseOut={(e) => {
                    e.target.style.borderColor = 'var(--text-muted)';
                    e.target.style.color = 'var(--text-muted)';
                }}
            >
                Analyze Another Article
            </button>
        </div >
    )
}
export default PredictionResult
