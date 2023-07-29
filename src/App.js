import React, { useState } from 'react';

function PromptInput({ onFormSubmit }) {
  const [input, setInput] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onFormSubmit(input);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Enter the topic for an argument..."
      />
      <button type="submit">Submit</button>
    </form>
  );
}

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [script, setScript] = useState(null);

  const handleFormSubmit = (topic) => {
    setIsLoading(true);
    fetch('http://localhost:5000/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({input: topic})
    })
    .then(response => response.json())
    .then(data => {
      setIsLoading(false);
      setScript(data.output);
    });
  };

  return (
    <div>
      <PromptInput onFormSubmit={handleFormSubmit} />
      {isLoading && <p>Loading...</p>}
      {script && <p>{script}</p>}
    </div>
  );
}


export default App;