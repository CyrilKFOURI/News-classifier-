export const classifyText = async (text) => {
    const API_URL = import.meta.env.VITE_API_URL;

    // Simulation Mode (Default if no API URL)
    if (!API_URL) {
        console.warn("Using Mock API Mode");
        return new Promise((resolve) => {
            setTimeout(() => {
                const categories = ["Tech", "Business", "Sport", "Politics", "Entertainment"];
                resolve({
                    category: categories[Math.floor(Math.random() * categories.length)],
                    confidence: (Math.random() * (0.99 - 0.70) + 0.70).toFixed(4)
                });
            }, 1500);
        });
    }

    // Real Mode
    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text }),
        });
        if (!response.ok) throw new Error("API Error");
        return await response.json();
    } catch (error) {
        console.error(error);
        throw error;
    }
};
