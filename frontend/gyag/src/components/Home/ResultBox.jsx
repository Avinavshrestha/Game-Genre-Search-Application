import React, { useEffect, useState } from 'react';
import ResultCard from './ResultCard';

function ResultBox({ searchQuery }) {
  const [results, setResults] = useState([]);
  const [hasSearched, setHasSearched] = useState(false); // New state to track search attempts

  useEffect(() => {
    const fetchResults = async () => {
      if (!searchQuery || searchQuery.trim() === '') return;

      const response = await fetch(`http://127.0.0.1:8000/search/?query=${searchQuery}`);
      const data = await response.json();
      setResults(data);
      setHasSearched(true); // Set hasSearched to true after fetching results
    };

    fetchResults();
  }, [searchQuery]);

  if  (!hasSearched) return null;


  return (
    <div className='max-h-[35rem] w-full flex flex-col gap-4 bg-[rgba(0,0,0,0.50)] rounded-xl p-8 overflow-y-auto'>
      {hasSearched && results.length === 0 ? ( // Only show message if a search has been attempted
        <p className="text-white text-center">No results found.</p>
      ) : (
        results.map((result, index) => (
          <ResultCard key={index} result={result} />
        ))
      )}
    </div>
  );
}

export default ResultBox;
