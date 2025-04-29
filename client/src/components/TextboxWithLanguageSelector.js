import React, { useState } from 'react';

function TextboxWithLanguageSelector() {
  const [selectedLanguage, setSelectedLanguage] = useState('cherokee');
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handleLanguageChange = (language) => {
    setSelectedLanguage(language);
  };

  const handleChange = (event) => {
    setText(event.target.value);
  };

  const handleConvert = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/${selectedLanguage}/${encodeURIComponent(text)}`);
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
      <h1 className="title">Transliteramajig</h1>
      <div className="language-selector">
        <button
          className={selectedLanguage === 'cherokee' ? 'active' : ''}
          onClick={() => handleLanguageChange('cherokee')}
          disabled={selectedLanguage === 'cherokee'}
        >
          Cherokee
        </button>
        <button
          className={selectedLanguage === 'vai' ? 'active' : ''}
          onClick={() => handleLanguageChange('vai')}
          disabled={selectedLanguage === 'vai'}
        >
          Vai
        </button>
      </div>
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

export default TextboxWithLanguageSelector;