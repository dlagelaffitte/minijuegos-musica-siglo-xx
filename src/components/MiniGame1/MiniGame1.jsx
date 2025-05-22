import React from 'react';
import composersData from '../../data/composers.json';

function MiniGame1() {
  return (
    <div>
      <h2>Compositores:</h2>
      <ul>
        {composersData.map((composer) => (
          <li key={composer.name}>{composer.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default MiniGame1;