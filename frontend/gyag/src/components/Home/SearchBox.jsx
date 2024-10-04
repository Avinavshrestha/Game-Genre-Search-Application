import React, { useState } from 'react';
import SearchIcon from './SearchIcon';

function SearchBox({ onSearch }) {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query);
  };

  return (
    <>
      <h1 className='text-6xl font-serif mb-10 text-white'>Game Genre</h1>
      <form onSubmit={handleSubmit} className='flex items-center gap-4'>
        <input
          className='h-12 w-[40rem] pl-8 rounded-xl focus-visible:outline-none text-lg bg-[rgba(0,0,0,0.50)] text-white'
          type="text"
          name='query'
          value={query}
          placeholder='Find your game genre'
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit" className=' h-12 w-12 flex justify-center items-center bg-[rgba(0,0,0,0.50)] rounded-xl hover:bg-[rgba(0,0,0,0.80)]'>
          <SearchIcon />
        </button>
      </form>
    </>
  );
}

export default SearchBox;
