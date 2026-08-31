import { Link } from "react-router-dom"

function SongCard(props: { key: string; isrc: string; image_url: string; title: string | null; artist: string | null; }) {
    return(
        <Link to={`/song/${props.isrc}`} className="song-card">
            <img className="song-image" src={props.image_url}></img>
            <div className="song-text-container">
                <h2>{props.title}</h2>
                <p>{props.artist}</p>
            </div>
        </Link>
    )
}

export default SongCard;