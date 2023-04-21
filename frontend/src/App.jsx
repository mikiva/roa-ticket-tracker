import { useState } from 'react'
import BaseList from './components/BaseList'
import CountdownTimer from './components/CountdownTimer'

function App() {

  return (
    <>
      <div className="bg-black w-screen h-screen relative bg-gradient-to-b from-black from-70%  to-orange-500/10">
        <img src={"src/assets/roa_color_splash.png"} alt="" className="max-w-xl -top-20 absolute left-0 right-0 m-[0_auto] z-0 w-full h-auto object-fit" />
        <img src={"src/assets/roa.png"} alt="" className="m-auto max-w-xs relative z-10 w-full" />
        <div className="flex flex-col justify-center max-w-xl m-auto relative z-20 pt-5">
          <CountdownTimer >
            <div className="text-6xl">PREMIÄR</div>
          </CountdownTimer>
          {false &&
            <div className="text-white flex justify-center pt-5">
              <div className="border-4 border-black rounded bg-slate-900/80 flex w-[96%] flex-col">
                <BaseList>
                  <div className="text-lg font-bold w-full border-b">Sålda</div>

                </BaseList>

              </div>
            </div>
          }
        </div>
      </div>
    </>
  )
}

export default App
