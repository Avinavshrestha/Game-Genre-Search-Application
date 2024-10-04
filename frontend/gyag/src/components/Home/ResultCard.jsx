import React, { useState } from 'react';

function ResultCard({ result }) {
  // State to manage the description toggle
  const [isExpanded, setIsExpanded] = useState(false);

  // Function to handle the toggle
  const toggleDescription = () => {
    setIsExpanded(!isExpanded);
  };

  // Check if the description exceeds 50 characters
  const isLongDescription = result.description.length > 50;
  const displayedDescription = isExpanded ? result.description : result.description.slice(0, 50) + (isLongDescription ? '...' : '');
  const displayType = isExpanded ? "block" : "flex";
  return (
    <div className="bg-[rgba(155,155,155,0.81)] p-4 w-full rounded-lg">
      <div className="flex gap-2 w-full justify-between mb-2">
        <p className="text-3xl">{result.title}</p>
        <p className="text-xl font-light">Score: {result.score.toFixed(2)}</p>
      </div>
      <div className={displayType}>
        <p className="max-w-[35rem] text-lg text-wrap font-light mb-2">{displayedDescription}</p>
        {isLongDescription && (
            <button
            onClick={toggleDescription}
            className="underline mb-2"
            >
            {isExpanded ? 'See Less' : 'See More'}
            </button>
        )}
      </div>

      <p className="mb-2 text-lg">Recommended Games</p>
      <div className="flex flex-wrap gap-2 max-w-[35rem]">
        {result.games.split(', ').map((game, index) => (
          <p key={index} className="bg-[rgba(0,0,0,0.80)] w-fit p-2 rounded-lg text-white font-light">{game}</p>
        ))}
      </div>
    </div>
  );
}

export default ResultCard;
