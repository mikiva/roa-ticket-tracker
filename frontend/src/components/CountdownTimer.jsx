import { useEffect, useState } from "react";


export default function CountdownTimer({ children }) {

    const targetDate = new Date("2023-10-14T15:00:00").getTime()
    const [current, setCurrent] = useState(
        getCount()
    )

    function getCount() {
        const now = new Date().getTime()
        const difference = (targetDate - now) / 1000

        let days = Math.floor(difference / (60 * 60 * 24));
        let hours = Math.floor((difference % (60 * 60 * 24)) / (60 * 60));
        let minutes = Math.floor((difference % (60 * 60)) / 60);
        let seconds = Math.floor(difference % 60);

        return {
            days: days,
            hours: hours,
            minutes: minutes,
            seconds: seconds
        }

    }

    function countDown() {
        setCurrent(getCount());
    }

    useEffect(() => {
        const timer = setInterval(countDown, 1000);


        return () => clearInterval(timer)


    }, [])
    const day = current["days"] === 1 ? "dag" : "dagar";
    const hour = current["hours"] === 1 ? "timme" : "timmar";
    const minute = current["minutes"] === 1 ? "minut" : "minuter";
    const second = current["seconds"] === 1 ? "sekund" : "sekunder";

    return (
        <div className="text-white text-center bg-black/50 w-full border-black border-2 py-2 px-5">
            {children}

            <div className="flex gap-2 text-white text-lg  flex-nowrap justify-around leading-none">
                <TimePart time={current["days"]} unit={day} />
                <TimePart time={current["hours"]} unit={hour} />
                <TimePart time={current["minutes"]} unit={minute} />
                <TimePart time={current["seconds"]} unit={second} />

            </div>
        </div>
    )


}

function TimePart({ time, unit }) {
    return (
        <div className="text-center">
            <div className="text-5xl">{time}</div>
            <div className="text-sm text-orange-500">{unit}</div>
        </div>
    )
}