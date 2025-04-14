
### frontend/src/App.js
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [userId, setUserId] = useState('user1');
  const [recommendations, setRecommendations] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [similarProducts, setSimilarProducts] = useState([]);

  const fetchRecommendations = async () => {
    const res = await fetch(`http://localhost:8000/recommend/user/${userId}`);
    const data = await res.json();
    setRecommendations(data.recommendations || []);
    setSelectedProduct(null);
    setSimilarProducts([]);
  };

  const fetchSimilarProducts = async (productId) => {
    const res = await fetch(`http://localhost:8000/recommend/product/${productId}`);
    const data = await res.json();
    setSimilarProducts(data.similar_products || []);
  };

  useEffect(() => {
    fetchRecommendations();
  }, [userId]);

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Product Recommendations</h1>

      <label className="block mb-2">Enter User ID:</label>
      <input
        className="border px-2 py-1 mb-4 w-full"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      />

      <button
        onClick={fetchRecommendations}
        className="bg-blue-500 text-white px-4 py-2 rounded mb-4"
      >
        Get Recommendations
      </button>

      <h2 className="text-xl font-semibold mb-2">Recommended Products:</h2>
      <ul>
        {recommendations.map((item, idx) => (
          <li
            key={idx}
            className="border p-2 mb-2 rounded shadow cursor-pointer hover:bg-gray-100"
            onClick={() => {
              setSelectedProduct(item);
              fetchSimilarProducts(item.product_id);
            }}
          >
            <h3 className="font-semibold">{item.name}</h3>
            <p>{item.description}</p>
          </li>
        ))}
      </ul>

      {selectedProduct && (
        <div className="mt-6">
          <h2 className="text-xl font-bold mb-2">Similar to: {selectedProduct.name}</h2>
          <ul>
            {similarProducts.map((item, idx) => (
              <li key={idx} className="border p-2 mb-2 rounded shadow">
                <h3 className="font-semibold">{item.name}</h3>
                <p>{item.description}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;


### frontend/src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);


### frontend/tailwind.config.js
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};


### frontend/package.json
{
  "name": "frontend",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}


### frontend/src/index.css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  font-family: sans-serif;
  background-color: #f9fafb;
}
