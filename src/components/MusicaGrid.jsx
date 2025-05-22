import React, { useState, useEffect } from 'react';
// Importa los datos JSON
import composers from '../data/composers.json';
import styles from '../data/styles.json';
// import paintings from '../data/paintings.json'; // Si tienes datos de pinturas
// import relationships from '../data/relationships.json'; // Si quieres relaciones extra
import './MusicaGrid.css'; // Crea este archivo para los estilos

// Utilidad para mezclar arrays
function shuffle(array) {
  return array
    .map(value => ({ value, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ value }) => value);
}

const GRID_SIZE = 4; // Cambia a 3 para un tablero 3x3

// Genera preguntas aleatorias para el grid
function generateGridData() {
  // Mezcla los datos y selecciona algunos para el grid
  const selectedComposers = shuffle(composers).slice(0, GRID_SIZE);
  const selectedStyles = shuffle(styles).slice(0, GRID_SIZE);

  // Crea pares de pregunta-respuesta
  const questions = [];

  for (let i = 0; i < GRID_SIZE; i++) {
    questions.push({
      type: 'composer-style',
      question: `¿Qué estilo musical corresponde a ${selectedComposers[i].name}?`,
      answer: selectedComposers[i].style,
      options: shuffle(selectedStyles.map(s => s.name)).slice(0, 3).concat(selectedComposers[i].style)
    });
  }

  for (let i = 0; i < GRID_SIZE; i++) {
    questions.push({
      type: 'style-composer',
      question: `¿Quién es un compositor representativo del estilo ${selectedStyles[i].name}?`,
      answer: selectedStyles[i].composers[0], // El primero de la lista
      options: shuffle(selectedComposers.map(c => c.name)).slice(0, 3).concat(selectedStyles[i].composers[0])
    });
  }

  // Mezcla todas las preguntas
  return shuffle(questions).slice(0, GRID_SIZE * GRID_SIZE);
}

function MusicaGrid() {
  const [gridData, setGridData] = useState([]);
  const [userAnswers, setUserAnswers] = useState(Array(GRID_SIZE * GRID_SIZE).fill(null));
  const [results, setResults] = useState(Array(GRID_SIZE * GRID_SIZE).fill(null));
  const [showResults, setShowResults] = useState(false);

  useEffect(() => {
    setGridData(generateGridData());
  }, []);

  // Maneja la selección del usuario
  const handleSelect = (cellIdx, selectedOption) => {
    const newAnswers = [...userAnswers];
    newAnswers[cellIdx] = selectedOption;
    setUserAnswers(newAnswers);
  };

  // Valida las respuestas
  const checkAnswers = () => {
    const newResults = gridData.map((cell, idx) => userAnswers[idx] === cell.answer);
    setResults(newResults);
    setShowResults(true);
  };

  // Reinicia el juego
  const resetGame = () => {
    setGridData(generateGridData());
    setUserAnswers(Array(GRID_SIZE * GRID_SIZE).fill(null));
    setResults(Array(GRID_SIZE * GRID_SIZE).fill(null));
    setShowResults(false);
  };

  return (
    <div className="musica-grid-container">
      <h2>Música Grid</h2>
      <div className="instructions">
        <strong>Instrucciones:</strong>
        <ul>
          <li>Responde cada pregunta del tablero seleccionando la opción correcta.</li>
          <li>Haz clic en "Comprobar" para ver tus aciertos y errores.</li>
          <li>Las celdas verdes son correctas, las rojas incorrectas.</li>
          <li>Puedes reiniciar el juego para intentarlo de nuevo.</li>
        </ul>
      </div>
      <div
        className="musica-grid"
        style={{
          gridTemplateColumns: `repeat(${GRID_SIZE}, 1fr)`,
          gridTemplateRows: `repeat(${GRID_SIZE}, 1fr)`
        }}
      >
        {gridData.map((cell, idx) => (
          <div
            key={idx}
            className={`musica-cell ${
              showResults
                ? results[idx]
                  ? 'correct'
                  : 'incorrect'
                : ''
            }`}
          >
            <div className="question">{cell.question}</div>
            <select
              value={userAnswers[idx] || ''}
              onChange={e => handleSelect(idx, e.target.value)}
              disabled={showResults}
            >
              <option value="">Selecciona una opción</option>
              {shuffle(cell.options).map((option, i) => (
                <option value={option} key={i}>
                  {option}
                </option>
              ))}
            </select>
            {showResults && (
              <div className="feedback">
                {results[idx] ? '✔️ Correcto' : `❌ Incorrecto (Respuesta: ${cell.answer})`}
              </div>
            )}
          </div>
        ))}
      </div>
      <div className="musica-grid-actions">
        {!showResults && (
          <button onClick={checkAnswers} className="check-btn">
            Comprobar
          </button>
        )}
        {showResults && (
          <button onClick={resetGame} className="reset-btn">
            Reiniciar
          </button>
        )}
      </div>
    </div>
  );
}

export default MusicaGrid;