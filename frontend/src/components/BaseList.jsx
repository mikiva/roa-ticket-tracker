

const shows = [
    {
        date: new Date().toISOString(),
        sold: 132
    },
    {
        date: new Date().toISOString(),
        sold: 321
    }
]

export default function BaseList({ children }) {
    return (
        <>
            <div className="flex flex-col">
                {children}
                {shows.map((s, idx) => <ListItem show={s} key={idx} />)}
            </div>
        </>
    )
}


function ListItem({ show }) {
    const { date, sold } = show;
    return (
        <div className="grid grid-cols-2 border-b py-3">
            <div>{date}</div>
            <div>{sold}</div>
        </div>
    )
}