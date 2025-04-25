import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');

  const handleChange = (event) => {
    setText(event.target.value);
  };

  return (
    <div className="default-textbox">
      <textarea
        value={text}
        onChange={handleChange}
        placeholder="Enter your text here..."
        rows="10"
        cols="50"
      />
    </div>
  );
}

export default App;