import { useState} from "react";
import type { Song } from "./types/Song";
import SongCard from "./SongCard.tsx";

// URL for backend API
const URL = "http://localhost:8000/songs"

function SearchBar() {

    const[songs, setSongs] = useState<Song[]>([])
    const[query, setQuery] = useState("")

    async function fetchSongs() {
            const result = await fetch(`${URL}/?query=${encodeURIComponent(query)}`)

            const json_result = await result.json()

            // Get list of songs and set to variable songs
            setSongs(json_result.songs)
        }

    function searchSongs(event: React.SubmitEvent) {
        event.preventDefault() // Stops default actions of creating new request when submitting
        fetchSongs()
    }

    return (
        <div className="song-search-container">
            <form onSubmit={searchSongs}>
                <input
                    className="song-search-bar"
                    type="search"
                    id="search-input"
                    placeholder="Search Songs..."
                    value={query}
                    onChange={(event) => setQuery(event.target.value)}
                />
                <button type="submit">Search</button>
            </form>
            <div className="song-card-grid">
                {songs.map((song) => (
                    <SongCard key={song.isrc} isrc={song.isrc} title={song.title} artist={song.artist} image_url={song.album_cover_url}/>
                ))}
            </div>

        </div>

    )
}

export default SearchBar