import React, { useState } from 'react';

function TextboxWithButton() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handleChange = (event) => {
    setText(event.target.value);
  };

  const handleConvert = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/cherokee/${encodeURIComponent(text)}`);
      if (response.ok) {
        const data = await response.text();
        console.log('Conversion result:', data);
        setResult(data);
      } else {
        console.log('Error: Unable to fetch conversion.');
        setResult('Error: Unable to fetch conversion.');
      }
    } catch (error) {
      console.log('Error: Unable to fetch conversion.');
      setResult('Error: Unable to fetch conversion.');
    }
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
      <button onClick={handleConvert}>Convert</button>
      {result && <div className="result-box">{result}</div>}
    </div>
  );
}

export default TextboxWithButton;