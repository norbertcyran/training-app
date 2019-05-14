import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const Table = ({data}) =>
    !data.length ? (
        <p>Loading data</p>
    ) : (
        <div className="column">
            <h2 className="subtitle">
                Showing {data.length} from {data.length} excercises.
            </h2>
            <table>
                <tbody>
                {data.map(el => (
                    <tr key={el.id}>
                    {/* @TODO: replace hardcoded src by el.image and 'alt also' */}
                        <td><img src="https://dummyimage.com/100x100/0010f0/cccccc&text=image+is+comming" alt="alttxt"></img></td>
                        {Object.entries(el).map(el => <td key={key(el)}>{el[1]}</td>)}
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );

Table.propTypes = {
    data: PropTypes.array.isRequired
};

export default Table
