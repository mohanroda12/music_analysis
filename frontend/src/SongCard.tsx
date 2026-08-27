function SongCard(props: { image_url: string; title: string | null; artist: string | null; }) {

    return(
        <div className="song-card">
            <img className="song-image" src={props.image_url}></img>
            <div className="song-text-container">
                <h2>{props.title}</h2>
                <p>{props.artist}</p>
            </div>
        </div>
    )
}

export default SongCard;