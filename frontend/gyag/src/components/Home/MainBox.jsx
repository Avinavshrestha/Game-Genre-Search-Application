import React, { useState } from 'react';
import ResultBox from './ResultBox';
import SearchBox from "./SearchBox";

function MainBox() {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = (query) => {
    setSearchQuery(query);
  };

  return (
    <div className='flex flex-col gap-5 items-center bg-[rgba(155,155,155,0.21)] shadow-lg p-10 rounded-2xl '>
      <SearchBox onSearch={handleSearch} />
      <ResultBox searchQuery={searchQuery} />
    </div>
  );
}

export default MainBox;
