import React from 'react';
import MainBox from './components/Home/MainBox'; // Ensure the path is correct

function App() {
  return (
    <>
      <div
        className="absolute inset-0 bg-gray-800 bg-cover bg-center blur-sm" // Overlay with reduced opacity
        style={{backgroundImage: 'url("/background.jpg")' }}
      />
      <div className='h-screen w-screen absolute bg-black opacity-50'></div>
      <main className="h-screen w-screen flex justify-center items-center relative z-20">
        <MainBox />
      </main>
    </>
  );
}

export default App;
